from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
    {"info": "bold cyan", "warning": "magenta", "danger": "bold red"}
)
console = Console(theme=custom_theme)
console.print("The Gostak distims the doshes", style="info")
console.print("All your bases are belong to us", style="warning")
console.print("Klingons on the starboard bow!", style="danger")
