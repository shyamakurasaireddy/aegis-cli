from rich.console import Console

console = Console()

def main():
    console.print("[bold green] Ageis CLI [/bold green]")
    console.print("Status: experimental")
    console.print("Type 'exit' to quit")

    while True:
        try:
            user = input("aegis > ").strip()
            if user in ("exit","quit"):
                break
            console.print(f"You said: {user}")
        except KeyboardInterrupt:
            break