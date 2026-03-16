"""

This file controls the Menu for the Sampling proyect

Created by:

 _____         _         _          _          ___        _
/  __ \       | |       | |        | |        / _ \      | |
| /  \/  __ _ | |  __ _ | | __   __| |  ___  / /_\ \ ___ | |_   ___   _ __   __ _
| |     / _` || | / _` || |/ /  / _` | / _ \ |  _  |/ __|| __| / _ \ | '__| / _` |
| \__/\| (_| || || (_| ||   <  | (_| ||  __/ | | | |\__ \| |_ | (_) || |   | (_| |
 \____/ \__,_||_| \__,_||_|\_\  \__,_| \___| \_| |_/|___/ \__| \___/ |_|    \__,_|

elcalak gh: https://github.com/elcalak 

Suggest:
Compile in environment: Use Environment.sh to install all dependencies

"""

from rich.console import Console
import menu

console = Console() #Create console object from rich library
console.clear() #Clear console

TITLE = r"""
        
 ██████╗ █████╗ ██╗      █████╗ ██╗  ██╗    ██████╗ ███████╗     █████╗ ███████╗████████╗ ██████╗ ██████╗  █████╗ 
██╔════╝██╔══██╗██║     ██╔══██╗██║ ██╔╝    ██╔══██╗██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗
██║     ███████║██║     ███████║█████╔╝     ██║  ██║█████╗      ███████║███████╗   ██║   ██║   ██║██████╔╝███████║
██║     ██╔══██║██║     ██╔══██║██╔═██╗     ██║  ██║██╔══╝      ██╔══██║╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║
╚██████╗██║  ██║███████╗██║  ██║██║  ██╗    ██████╔╝███████╗    ██║  ██║███████║   ██║   ╚██████╔╝██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                 
""" #Title ascii art
console.rule(title = "Development by: ", characters = "=") #Print rule with rich library
console.print(TITLE, style="bold blue", justify="center") #Print title with rich style
console.rule(title = "Christopher G. Linares", characters = "=") #Print rule with rich library

while True:

    menu = menu.Menu() #Create object Menu

    opti = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number

    menu.menu_controls(opti) #Call menucontrols function with option parameter
