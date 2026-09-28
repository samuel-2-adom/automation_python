from datetime import datetime
from turtle import title
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.padding import Padding
from rich.prompt import Confirm
from rich.prompt import Prompt
console = Console()
# Get Date and Time


def format():
    now = datetime.now()
    return now.strftime("%Y-%m-%d | %I:%M:%S %p")



# Rich UI design for the CLI interface
def render_screen_weather():
    title = "    ⚡ MY TOOL "
    subtitle = "API_CLIENT CLI Interface"
    
    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()


    header = Text(title, style=f"bold {header_color}")
    sub = Text(subtitle, style=accent_color)

    console.print(
        Padding(
            Panel(
                Align.center(header + "\n" + sub),
                border_style=header_color
            ),
            (1, 2)
        )
    )


    #***********************************************

    menu = Group(
    " [yellow][1][/yellow]  [cyan]Current Weather / Forcast[/cyan] 🌤️",
    " [yellow][2][/yellow]  [cyan]Exchange Rate[/cyan] 🚚",
    " [yellow][3][/yellow]  [cyan]Github[/cyan] ✏️",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]MAIN OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #**************************************************

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{format()}")
    console.print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def render(sub):

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    f" [cyan]{sub} 👈[/cyan]",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="",
            title_align="center",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #**************************************************

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{format()}")
    console.print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))

if __name__ == "__main__":
    render_screen_weather()

    render("Weather Main") 