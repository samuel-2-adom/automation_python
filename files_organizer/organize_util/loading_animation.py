import time
from rich.progress import Progress, SpinnerColumn, TextColumn

#Loading animation
def loading_animation(pref="Loading interface...",duration=0):
    with Progress(
        SpinnerColumn(),
        TextColumn(f"[bold green]{pref}"),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)

if __name__ == "__main__":
    loading_animation(2)  # Show the loading animation for 2 seconds