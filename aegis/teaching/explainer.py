import shlex
from aegis.core.modes import Mode

COMMON_COMMANDS = {
    "ls": "List directory contents",
    "cd": "Change the current directory",
    "pwd": "Show the current working directory",
    "cp": "Copy files or directories",
    "mv": "Move or rename files",
    "rm": "Remove files or directories",
    "mkdir": "Create directories",
    "chmod": "Change file permissions",
    "chown": "Change file ownership",
    "cat": "Display file contents",
    "echo": "Print text to standard output",
}


def looks_like_command(text: str) -> bool:
    if not text:
        return False
    return text.strip().split()[0] in COMMON_COMMANDS


def explain_command(command: str, mode: Mode) -> str:
    try:
        parts = shlex.split(command)
    except ValueError:
        return "Unable to parse command. Check quoting or syntax."

    if not parts:
        return "Empty command."

    cmd = parts[0]
    args = parts[1:]

    lines = []

    # --- Command ---
    lines.append("Command")
    lines.append(f"  {cmd} — {COMMON_COMMANDS.get(cmd, 'Unknown command')}")
    lines.append("")

    # --- Usage ---
    lines.append("Usage")
    lines.append(f"  {command}")
    lines.append("")

    # --- Breakdown ---
    lines.append("Breakdown")
    lines.append(f"  - {cmd} : {COMMON_COMMANDS.get(cmd)}")

    for arg in args:
        if arg.startswith("-"):
            lines.append(f"  - {arg} : option/flag")
        else:
            lines.append(f"  - {arg} : argument")

    lines.append("")

    # --- Behavior ---
    lines.append("Behavior")
    lines.append("  This command does not modify system state.")
    lines.append("")

    return "\n".join(lines)
