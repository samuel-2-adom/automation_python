from time import strftime
from datetime import datetime
import time
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
def render_screen_main():
    title = "    ⚡ MY TOOL "
    subtitle = "Organizer CLI Interface"
    
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
    " [yellow][0][/yellow] 🏃 [cyan]Exit Organizer[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] 📋 [cyan]Copy[/cyan]",
    " [yellow][2][/yellow] 🚚 [cyan]Move[/cyan]",
    " [yellow][3][/yellow] ✏️  [cyan]Rename[/cyan]",
    " [yellow][4][/yellow] 🗑️  [cyan]Trash[/cyan]",
    " [yellow][5][/yellow] 🧩 [cyan]Parser[/cyan]",

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


def render_screen_copy():

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Copy[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] 📋 [cyan]Copy File[/cyan]",
    " [yellow][2][/yellow] 📁 [cyan]Copy Dir(Tree)[/cyan]",
    " [yellow][3][/yellow] 🏷️  [cyan]Copy Selected File(s) (Name/Ext)[/cyan]",

)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]COPY OPTIONS",
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


def render_screen_move():

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Move[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] 🚚 [cyan]Move File[/cyan]",
    " [yellow][2][/yellow] 🗂️  [cyan]Move Dir(Tree)[/cyan]",
    " [yellow][3][/yellow] 🏷️  [cyan]Move Selected File(s) (Name/Ext)[/cyan]",

)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]MOVE OPTIONS",
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

def render_screen_rename():

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Rename[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] ✏️  [cyan]Rename File/Directory[/cyan]",
    " [yellow][2][/yellow] 🏷️  [cyan]Rename Selected File(s) (Prefix) (Name/Ext)[/cyan]",

)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]RENAME OPTIONS",
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


def render_screen_trash():

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Trash[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] 🗑️  [cyan]Trash Path(File/Dir(Tree))[/cyan]",
    " [yellow][2][/yellow] 🚮 [cyan]Trash Selected File(s) (Name/Ext)[/cyan]",

)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]TRASH OPTIONS",
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


def render_screen_parse():

    header_color = "bright_magenta"
    box_color = "gold"
    accent_color = "bright_green"
    
    console.clear()

    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Parse[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][1][/yellow] 🔍 [cyan]Parse Dir(Series(Season/Episode))[/cyan]",

)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]PARSE OPTIONS",
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

if __name__ == "__main__":
    render_screen_main()
    print()
    render_screen_copy()
    print()
    render_screen_move()
    print()
    render_screen_rename()
    print()
    render_screen_trash()
    print()
    render_screen_parse()