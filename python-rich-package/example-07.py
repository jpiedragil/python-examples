from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
    {"info": "bold cyan", "warning": "magenta", "danger": "bold red"}
)
console = Console(theme=custom_theme)
console.log("Nothing happening here", style="info")
console.log("Trouble brewing...", style="warning")
console.log("Bad news!", style="danger")

raise RuntimeError("Things haven't worked out as we hoped")
