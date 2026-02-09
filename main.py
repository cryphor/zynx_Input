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
logo = """[bold purple]
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
    print("[bold purple][1]View Offsets")
    print("[bold purple][2]IP Lookup")
    print("[bold purple][3]Lookup")
    
    
    # -----------------
    quit = print("[bold bright_red]Type 'quit' to exit the program")
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
            
    if x == "3":
        print("LOOKUP\n")
        choice3 = """
                [bold purple][1]Roblox
                [bold purple][2]Discord (Really fucking trash rn im to lazy to fix it rn.)
        """
        print(choice3)
        x3 = input(f"[$]: ")
        
        if x3 == "1":
            os.system("cls")
            userid = input("Enter Roblox UID: ")
            r = requests.get(f"https://users.roblox.com/v1/users/{userid}")
            data = r.json()
            
            # info
            box = Panel.fit(renderable= f"[bold purple]Username: {data['name']}\nDisplay Name: {data['displayName']}\nCreated: {data['created']}\nDescription: {data['description']}\nBanned: {data['isBanned']}\nVerified {data['hasVerifiedBadge']}\nCreated: {data['created']}", title = f"User: {data['id']}", border_style="purple", box=HEAVY)
            print(box)
            
            # pause
            pause = input("Press enter to continue...")
            
        if x3 == "2":
            os.system("cls")
            userid = input("Enter Discord UID: ")
            r = requests.get(f"https://api.cord.cat/api/v1/query/{userid}")
            data = r.json()
            
            # info
            box = Panel.fit(renderable= f"[bold purple]Userinfo: {data['userInfo']}", border_style="purple", box=HEAVY)
            print(box)
            
            pause = input("Press enter to continue...")
        
    
    if x == "quit":
        os.system("cls")
        break