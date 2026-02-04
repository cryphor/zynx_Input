import requests
import os
import json
from rich import print, pretty
from rich.table import Table
from rich.panel import Panel
from rich.box import HEAVY
from rich.console import Console
from rich import print, panel

# logo
logo = """[bold cyan]
███╗   ██╗███████╗███████╗███████╗███████╗███████╗███████╗
████╗  ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██╔██╗ ██║█████╗  ███████╗█████╗  ███████╗█████╗  ███████╗
██║╚██╗██║██╔══╝  ╚════██║██╔══╝  ╚════██║██╔══╝  ╚════██║
██║ ╚████║███████╗███████║███████╗███████║███████╗███████║
╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝

"""

# main
while True:
    os.system("NESSES")
    os.system("cls")
    print(logo)
    print("[bold cyan][1]. View Offsets[/bold cyan]")
    print("[bold cyan][2]. IP Lookup[/bold cyan]")
    
    
    # -----------------
    quit = print("[bold red]Type 'quit' to exit the program")
    x = input(f"[$]: ")

    if x == "1":
        print(requests.get("https://offsets.ntgetwritewatch.workers.dev/offsets.hpp").text)
        pause = input("Press [Enter] to continue... ")
        
    if x == "2":
        print("IP LOOKUP\n")
        ip = input("Enter IP Address: ")
        if not ip:
            print("This aint a ip address bro")
        else:
            os.system("cls")
            r = requests.get(f"https://ipinfo.io/json/{ip}")
            data = r.json()

            table = Table(title="IP Information", box=HEAVY)
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="magenta")
            for key, value in data.items():
                table.add_row(key, str(value))
            console = Console()
            console.print(table)
            pause = input("Press [Enter] to continue... ")
    
    if x == "quit":
        os.system("cls")
        break