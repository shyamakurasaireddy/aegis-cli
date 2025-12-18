from rich.console import Console
from aegis.core.modes import Mode
import os
from aegis.core.config import Config
from aegis.core.context import Context


console = Console()

def main():
    config = Config()
    mode = Mode(config.get("mode","learning"))
    context = Context(mode)

    console.print("[bold green] Ageis CLI [/bold green]")
    console.print("Status: experimental")
    console.print(f"Mode: {mode.value}")
    console.print("Type 'exit' to quit")
    console.print("Switch mode with: mode learning | assisted | auto")

    while True:
        try:
            context.update_cwd()
            user = input(
                f"[aegis][{context.mode.value}][{context.cwd}]>").strip()

            if user in ("exit","quit"):
                break
            

            if user.startswith("mode "):
                _, new_mode = user.split(maxsplit=1)
                new_mode = new_mode.strip().lower()

                if new_mode in [m.value for m in Mode]:
                    mode = Mode(new_mode)
                    context.set_mode(mode)
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
                
            context.add_history(user)
            console.print(f"You said: {user}")
            
        except KeyboardInterrupt:
            break
           