import time
from rich.console import Console


def do_something_important():
    time.sleep(5.0)  # Simulates a long process


console = Console()
with console.status(
        "Please wait - solving global problems...", spinner="earth"
):
    do_something_important()

console.print("All fixed! :sunglasses:")
