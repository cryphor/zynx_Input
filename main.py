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
logo = """[bold red]
███████╗██╗   ██╗███╗   ██╗██╗  ██╗        ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗
╚══███╔╝╚██╗ ██╔╝████╗  ██║╚██╗██╔╝        ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝
  ███╔╝  ╚████╔╝ ██╔██╗ ██║ ╚███╔╝         ██║██╔██╗ ██║██████╔╝██║   ██║   ██║   
 ███╔╝    ╚██╔╝  ██║╚██╗██║ ██╔██╗         ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║   
███████╗   ██║   ██║ ╚████║██╔╝ ██╗███████╗██║██║ ╚████║██║     ╚██████╔╝   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝   

"""

# main
while True:
    os.system("ZYNX_INPUT")
    os.system("cls")
    print(logo)
    print("[bold red][1]. View Offsets[/bold red]")
    print("[bold red][2]. IP Lookup[/bold red]")
    
    
    # -----------------
    quit = print("[bold yellow]Type 'quit' to exit the program")
    x = input(f"[$]: ")

    if x == "1":
        os.system("cls")
        print(requests.get("https://offsets.ntgetwritewatch.workers.dev/offsets.hpp").text)
        pause = input("Press enter to continue... ")
        
    if x == "2":
        print("IP LOOKUP\n")
        ip = input("Enter IP Address: ")
        if not ip:
            print("This aint a ip address bro")
        else:
            os.system("cls")
            r = requests.get(f"https://ipinfo.io/{ip}")
            data = r.json()
            
            # table
            table = Table(title="IP Information", box=HEAVY)
            table.add_column("Property", style="cyan")
            value = table.add_column("Info", style="magenta")
            
            # rows
            for key, value in data.items():
                table.add_row(key, str(value))
            console = Console()
            console.print(table)
            pause = input("Press enter to continue... ")
    
    if x == "quit":
        os.system("cls")
        break