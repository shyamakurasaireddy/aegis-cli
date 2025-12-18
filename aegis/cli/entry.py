from rich.console import Console
from pathlib import Path

from aegis.core.modes import Mode
from aegis.core.config import Config
from aegis.core.context import Context
from aegis.teaching.explainer import looks_like_command, explain_command


console = Console()


def mode_style(mode: Mode) -> str:
    if mode == Mode.LEARNING:
        return "blue"
    if mode == Mode.ASSISTED:
        return "yellow"
    if mode == Mode.AUTO:
        return "red"
    return "white"


def short_path(path: str) -> str:
    home = str(Path.home())
    if path.startswith(home):
        path = path.replace(home, "~", 1)

    parts = path.rstrip("/").split("/")
    if len(parts) > 1:
        return parts[-1] if parts[-1] else "/"
    return path


def main():
    config = Config()
    context = Context(Mode(config.get("mode", "learning")))

    console.print("[bold green]Aegis CLI[/bold green]")
    console.print("Status: experimental")
    console.print("Type 'exit' to quit")

    console.print("\n[bold]Modes:[/bold]")
    console.print("  [blue]learning[/blue]  → explain commands only (safe)")
    console.print("  [yellow]assisted[/yellow] → suggest commands before execution")
    console.print("  [red]auto[/red]      → plan or run commands automatically\n")

    while True:
        try:
            context.update_cwd()
            display_path = short_path(context.cwd)
            style = mode_style(context.mode)

            user = console.input(
                f"[bold cyan]aegis[/bold cyan] "
                f"[{style}][{context.mode.value}][/{style}] "
                f"[green]{display_path}[/green] ❯ "
            ).strip()

            if user in ("exit", "quit"):
                break

            # --- Mode switching ---
            if user.startswith("mode "):
                _, new_mode = user.split(maxsplit=1)
                new_mode = new_mode.strip().lower()

                if new_mode in [m.value for m in Mode]:
                    context.set_mode(Mode(new_mode))
                    config.set("mode", new_mode)
                    console.print(f"[green]Switched to {new_mode} mode[/green]")
                else:
                    console.print(
                        "[red]Invalid mode.[/red] "
                        "Valid modes: learning, assisted, auto"
                    )
                continue

            context.add_history(user)

            # --- Teaching behavior ---
            if context.mode == Mode.LEARNING and looks_like_command(user):
                console.print(explain_command(user, context.mode))
                continue

            # --- Mode-aware fallback ---
            if looks_like_command(user):
                console.print(
                    f"[dim]{context.mode.value} mode:[/dim] "
                    "command detected."
                )
            else:
                console.print(f"[dim]Not a command:[/dim] {user}")

        except KeyboardInterrupt:
            break
