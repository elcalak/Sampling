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
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk

"""

import os #Import os library
from time import sleep #From module time import sleep function
import AudioBank as ab #Call the module from Control audio banks
import RecordSamp as rs #Call the module from Record Samples
import PlayMode as pm #Call the module from Play Modes
import EditSamp as es #Call the module from Edit Samples
from rich.console import Console #Import rich library as r for better terminal output

class Menu: #Start class Menu

    def __init__(self): #Init contructor for Menu
        
        console = Console() #Create console object from rich library
        
        print("Menu initialized") #Work check

        sleep(1) #Sleep 1 second
        console.clear() #Clear the terminal screen
        
        title = (r"""
        
        ███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗ 
        ██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██║████╗  ██║██╔════╝ 
        ███████╗███████║██╔████╔██║██████╔╝██║     ██║██╔██╗ ██║██║  ███╗
        ╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██║██║╚██╗██║██║   ██║
        ███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗██║██║ ╚████║╚██████╔╝
        ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                 
        """) #Title ascii art
        
        console.rule(title = "Welcome to: ", characters = "=") #Print rule with rich library
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        console.rule(title = "By: Calak de Astora", characters = "=") #Print rule with rich library
        #print("\n\tWelcome to Sampling Proyect") #Welcome message
        
        console.print("\nSelect an option:", style="bold", justify = "center") #Print select option message
        console.print("1. Sample Menu", style = "bold magenta", justify = "full") #Print option 1
        console.print("2. Audio Bank Menu", style = "bold magenta", justify = "full") #Print option 2
        console.print("0. Exit", style = "bold red", justify = "full") #Print option 3

    #End contructor

    def MenuControls(self, option): #Start function menucontrols with option parameter

        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            print("Sample Menu selected") #Print sample menu selected message
            console.clear() #Clear the terminal screen

            title = (r"""
            
███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
███████╗███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██╗
███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
            
            """) #Title ascii art

            console.rule(title = "You are in: Sampler Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Main Menu", characters = "=") #Print rule with rich library

            console.print("\nSelect an option:", style="bold", justify = "center") #Print select option message
            console.print("1. Record Mic Sample", style = "bold purple", justify = "full") #Print option 1
            console.print("2. Record Desk Sample", style = "bold purple", justify = "full") #Print option 2
            console.print("3. Easy Chop", style = "bold blue", justify = "full") #Print option 3
            console.print("4. Audio effects to sample", style = "bold green", justify = "full")
            console.print("0. Back", style = "bold yellow", justify = "full") #Print option 3
            
            new_option = int(console.input("\n[bold]Enter option number:[/bold] ")) #Input new option number
            self.MenuSample(new_option) #Call MenuSample function with new option parameter
            
        elif option == 2: #Else if option is 2
            
            print("AudioBank Menu selected") #Print sample menu selected message
            console.clear() #Clear the terminal screen

            title = (r"""

██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝
██████╔╝███████║██╔██╗ ██║█████╔╝ ███████╗
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ╚════██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                          
            """)

            console.rule(title = "You are in: Banks Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Main Menu", characters = "=") #Print rule with rich library

            console.print("\nSelect an option:", style="bold", justify = "full") #Print select option message
            console.print("1. Create Bank", style="bold white", justify = "full") #Print option 1
            console.print("2. Load Bank", style="bold blue", justify = "full") #Print option 2
            console.print("0. Back", style="bold yellow", justify = "full") #Print option 3
            
            new_option = int(console.input("\n[bold]Enter option number:[/bold] ")) #Input new option number
            self.MenuBank(new_option) #Call MenuBank function with new option parameter

        elif option == 0: #Else if option is 0
            
            print("Exiting...") #Print exiting message
            sleep(1) #Sleep 1 second
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            exit() #Exit the program

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(console.input("\n[bold]Enter option number:[/bold] ")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function again with new option parameter

    #End MenuControls

    def MenuSample(self, option): #Start function menusample with option parameter
        
        console = Console() #Create console object from rich library

        if option == 1: #If option is 1
            
            print("Record Mic Sample selected") #Print record sample selected message
            console.clear() #Clear the terminal screen

            title = (r"""
            
██████╗ ███████╗ ██████╗███╗   ███╗██╗ ██████╗██╗
██╔══██╗██╔════╝██╔════╝████╗ ████║██║██╔════╝██║
██████╔╝█████╗  ██║     ██╔████╔██║██║██║     ██║
██╔══██╗██╔══╝  ██║     ██║╚██╔╝██║██║██║     ╚═╝
██║  ██║███████╗╚██████╗██║ ╚═╝ ██║██║╚██████╗██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝
                                                                                             
            """)
            
            console.rule(title = "You are in: RecMic Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Sampler Menu", characters = "=") #Print rule with rich library

            option = int(console.input("\n[bold]Select time rec: [/bold]")) #Input option number
            rs.RecordSamp.RecMic(duration=option) #Call RecMic function from RecordSamp module with duration parameter

            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again

        elif option == 2: #Else if option is 2
            
            print("Record Desktop Sample selected") #Print record sample selected message
            console.clear() #Clear the terminal screen

            title = (r"""

██████╗ ███████╗ ██████╗██████╗ ███████╗███████╗██╗  ██╗██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝██║
██████╔╝█████╗  ██║     ██║  ██║█████╗  ███████╗█████╔╝ ██║
██╔══██╗██╔══╝  ██║     ██║  ██║██╔══╝  ╚════██║██╔═██╗ ╚═╝
██║  ██║███████╗╚██████╗██████╔╝███████╗███████║██║  ██╗██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝
                                                           
            """)

            console.rule(title = "You are in: RecDesk Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Sampler Menu", characters = "=") #Print rule with rich library

            print("WIP Coming soon...") #Print coming soon message
            sleep(3) #Sleep 3 seconds

            #option = int(input("\nSelect time rec: ")) #Input option number
            #rs.RecordSamp.RecDesk(duration=option) #Call RecMic function from RecordSamp module with duration parameter

            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again
        
        elif option == 3: #Else if option is 3
            
            EditSample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Chop Sample selected") #Print chop sample selected messages
            console.clear() #Clear the terminal screen

            title = (r"""
                
███████╗███████╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ██╗
██╔════╝╚══███╔╝██╔════╝██║  ██║██╔═══██╗██╔══██╗██║
█████╗    ███╔╝ ██║     ███████║██║   ██║██████╔╝██║
██╔══╝   ███╔╝  ██║     ██╔══██║██║   ██║██╔═══╝ ╚═╝
███████╗███████╗╚██████╗██║  ██║╚██████╔╝██║     ██╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ 
                                                                  
            """)
            
            console.rule(title = "You are in: EasyChop Menu", characters = "=") #Print rule with rich library
            console.print(title, style = "bold blue", justify = "center") #Print title with rich style
            console.rule(title = "Back to: Sampler Menu", characters = "=") #Print rule with rich library
            
            option = int(console.input("\n[bold]Select number of slices: [/bold]")) #Input option number
            EditSample.EzChop(num_slices=option) #Call Chop function from Record
            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again

        elif option == 4: #Else if option is 4

            print("Audio effects to sample Menu") #Print audio effects to sample selected message
            console.clear() #Clear the terminal screen

            title = (r"""
                     
███████╗███████╗███████╗███████╗ ██████╗████████╗███████╗
██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝
█████╗  █████╗  █████╗  █████╗  ██║        ██║   ███████╗
██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  ██║        ██║   ╚════██║
███████╗██║     ██║     ███████╗╚██████╗   ██║   ███████║
╚══════╝╚═╝     ╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝
                                                        
            """)
            
            console.rule(title = "You are in: Effects SubMenu", characters = "=") #Print rule with rich library
            console.print(title, style = "bold blue", justify = "center") #Print title with rich style
            console.rule(title = "Back to: Sampler Menu", characters = "=") #Print rule with rich library

            console.print("\nSelect an option:", style="bold", justify = "center") #Print select option message
            console.print("1. Pass Filter", style="bold black", justify = "full") #Print option 1
            console.print("2. Pitch Control", style="bold green", justify = "full") #Print option 2
            console.print("0. Back", style="bold yellow", justify = "full") #Print option 3

            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.EffectsSubMenu(option) #Call EffectsSubMenu function with option parameter
            self.MenuSample(4) #Call MenuSample function with option 4 parameter to show audio effects to sample menu again

        elif option == 0: #Else if option is 0
            
            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function with new option parameter

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuSample(new_option) #Call menusample function again with new option parameter

    #End MenuSample

    def EffectsSubMenu(self, option): #Start function effectsubmenu with option parameter
        
        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            EditSample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Filter Sample selected") #Print filter sample selected message
            console.clear() #Clear the terminal screen
            
            title = (r"""
                     
██╗  ██╗██████╗ ██╗    ██╗██╗     ██████╗ ██╗
██║  ██║██╔══██╗██║   ██╔╝██║     ██╔══██╗██║
███████║██████╔╝██║  ██╔╝ ██║     ██████╔╝██║
██╔══██║██╔═══╝ ╚═╝ ██╔╝  ██║     ██╔═══╝ ╚═╝
██║  ██║██║     ██╗██╔╝   ███████╗██║     ██╗
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    ╚══════╝╚═╝     ╚═╝ 
                                                                                        
            """)

            console.rule(title = "You are in: Filter Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Effects SubMenu", characters = "=") #Print rule with rich library

            EditSample.Catch(True) #Call Catch function from EditSamp object with True parameter to indicate it was called from the main menu

            self.MenuSample(4) #Call menucontrols function with option 1 parameter to show sample menu again

        elif option == 2: #if option is 2

            EditSample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Pitch Control selected") #Print pitch control selected message
            console.clear() #Clear the terminal screen

            title = (r"""

██████╗ ██╗████████╗ ██████╗██╗  ██╗██╗
██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║██║
██████╔╝██║   ██║   ██║     ███████║██║
██╔═══╝ ██║   ██║   ██║     ██╔══██║╚═╝
██║     ██║   ██║   ╚██████╗██║  ██║██╗
╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝

            """)  
            
            console.rule(title = "You are in: Pitch Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Effects SubMenu", characters = "=") #Print rule with rich library

            EditSample.Catch(False) #Call PitchControl function from EditSamp object with False parameter to indicate it was called from the main menu

            self.MenuSample(4) #Call menucontrols function with option 1 parameter to show sample menu again
        
        elif option == 0: #Else if option is 0
            
            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again

        else: #Else
            
            print("Invalid option") #Print invalid option message
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.EffectsSubMenu(new_option) #Call EffectsSubMenu function again with new option

    #End EffectsSubMenu

    def MenuBank(self, option): #Start function menubank with option parameter
        
        global backopt #Global variable to control back option in play menu
        backopt = 1 #Set backopt to 1 to control back option in play

        AudioBank = ab.AudioBank() #Create object AudioBank from AudioBank module
        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            print("\tCreate Bank") #Print create bank selected message
            console.clear() #Clear the terminal screen

            title = (r"""
                     
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ╚═╝
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                                    
            """)

            console.rule(title = "You are in: Bank Create Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Banks Menu", characters = "=") #Print rule with rich library

            sound = AudioBank.CreateBank() #Call CreateBank function from AudioBank object and saves the returned sounds
            
            if sound == None: #If sound is None it means that the user canceled the bank creation process and we need to go back to the bank menu
                
                console.print("\nBank creation canceled, going back to Banks Menu...", style="bold red", justify="center") #Print cancel message
                sleep(1) #Sleep 3 seconds
                self.MenuControls(2) #Call MenuBank function with option 2 parameter to show bank menu again
            
            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter

        elif option == 2: #Else if option is 2

            print("\tLoad Bank") #Print load bank selected message
            console.clear() #Clear the terminal screen

            title = (r"""

██╗      ██████╗  █████╗ ██████╗ 
██║     ██╔═══██╗██╔══██╗██╔══██╗
██║     ██║   ██║███████║██║  ██║
██║     ██║   ██║██╔══██║██║  ██║
███████╗╚██████╔╝██║  ██║██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                 
            """)

            console.rule(title = "You are in: Bank Load Menu", characters = "=") #Print rule with rich library
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            console.rule(title = "Back to: Banks Menu", characters = "=") #Print rule with rich library

            sound = AudioBank.LoadBank() #Call LoadBank function from AudioBank object

            if sound == None: #If sound is None it means that the user canceled the bank creation process and we need to go back to the bank menu
                
                console.print("\nBank Load canceled, going back to Banks Menu...", style="bold red", justify="center") #Print cancel message
                sleep(1) #Sleep 3 seconds
                self.MenuControls(2) #Call MenuBank function with option 2 parameter to show bank menu again

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter

        elif option == 0: #Else if option is 0
        
            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            new_option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function with new option parameter

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input new option number
            self.MenuBank(new_option) #Call menubank function again with new option parameter

    #End MenuBank

    def ShowPlayMenu(self): #Start function playmenu
        
        console = Console() #Create console object from rich library

        print("\tPlay Menu") #Print play menu message
        console.clear() #Clear the terminal screen
    
        title = (r"""
                 
██████╗ ██╗      █████╗ ██╗   ██╗██╗████████╗██╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║╚══██╔══╝██║
██████╔╝██║     ███████║ ╚████╔╝ ██║   ██║   ██║
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║   ██║   ╚═╝
██║     ███████╗██║  ██║   ██║   ██║   ██║   ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝
                                              
            """)

        console.rule(title = "You are in: Play Menu", characters = "=") #Print rule with rich library
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        console.rule(title = "Back to: Banks Menu", characters = "=") #Print rule with rich library
        
        console.print("\nSelect an option:", style="bold", justify="center") #Print select option message
        console.print("1. Finger Drumming", style="bold white", justify="full") #Print option 1
        console.print("2. Step Seq", style="bold blue", justify="full") #Print option 2
        console.print("0. Back", style="bold yellow", justify="full") #Print option 3

    #End ShowPlayMenu

    def PlayMenu(self, option, sound): #Start function playmenu with option and sound parameter

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        PlayMode = pm.PlayModes() #Create object PlayModes from PlayMode module
        console = Console() #Create console object from rich library

        if option == 1:#If option is 1:
        
            PlayMode.FingerDrum(sound) #Call FingerDrum function from PlayModes object with sound parameter

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter
            
        elif option == 2:
            
            PlayMode.StepSeq(sound) #Call StepSeq function from PlayModes object with sound parameter

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter
        
        elif option == 0: #Else if option is 0
            
            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            
            if backopt == 1:

                self.MenuControls(2) #Call menucontrols function with option 2 parameter to show audio bank menu again
                new_option = int(input("\n[bold]Enter option number: [/bold]")) #Input new option number
                self.MenuBank(new_option) #Call MenuBank function with new option parameter
            
            elif backopt == 0:
                
                self.MenuControls(1) #Call menucontrols function with option 2 parameter to show audio bank menu again
                new_option = int(input("\n[bold]Enter option number: [/bold]")) #Input new option number
                self.MenuBank(new_option) #Call MenuBank function with new option parameter

        else:
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\n[bold]Enter option number: [/bold]")) #Input new option number
            self.MenuBank(new_option) #Call menubank function again with new option parameter

    #End PlayMenu

#End class Menu

#These work chek lines go to the Main file (Maybe):

Menu = Menu() #Create object Menu

opti = int(input("\nEnter option number: ")) #Input option number

Menu.MenuControls(opti) #Call menucontrols function with option parameter

#End work chek lines