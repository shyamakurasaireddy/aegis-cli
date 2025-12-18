from rich.console import Console
from aegis.core.modes import Mode
import os
from aegis.core.config import Config

console = Console()

def main():
    config = Config()
    mode = Mode(config.get("mode","learning"))

    console.print("[bold green] Ageis CLI [/bold green]")
    console.print("Status: experimental")
    console.print(f"Mode: {mode.value}")
    console.print("Type 'exit' to quit")
    console.print("Switch mode with: mode learning | assisted | auto")

    while True:
        try:
            cwd = os.getcwd()
            user = input(f"[aegis][{mode.value}][{cwd}]>").strip()

            if user in ("exit","quit"):
                break

            if user.startswith("mode "):
                _, new_mode = user.split(maxsplit=1)
                new_mode = new_mode.strip().lower()

                if new_mode in [m.value for m in Mode]:
                    mode = Mode(new_mode)
                    config.set("mode",mode.value)
                    console.print(
                        f"[green]Switched to {mode.value} mode[/green]"
                    )
                else:
                    console.print(
                        "[red]Invalid mode.[/red] "
                        "Valid modes: learning, assisted, auto"
                    )
                continue

            console.print(f"You said: {user}")
        except KeyboardInterrupt:
            break
           