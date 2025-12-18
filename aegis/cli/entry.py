from rich.console import Console
from aegis.core.models import Mode
import os

console = Console()

def main():
    mode = Mode.LEARNING

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
                try:
                    model = Mode(new_mode)
                    console.print(f"[green] Switched to {mode.value} mode [/green]")
                except ValueError:
                    console.print("[red]Invalid mode[red]")
                continue

            console.print(f"You said: {user}")
        except KeyboardInterrupt:
            break
           