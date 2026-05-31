"""

This file controls the Menu for the Sampling proyect

Created by:

Calak de Astora gh: https://github.com/elcalak

Suggest:
Compile in environment: Use Environment.sh to install all dependencies
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk

"""

import os #Import os library
from time import sleep #From module time import sleep function
from rich.console import Console #Import rich library as r for better terminal output
import audio_bank as ab #Call the module from Control audio banks
import record_sample as rs #Call the module from Record Samples
import play_modes as pm #Call the module from Play Modes
import edit_sample as es #Call the module from Edit Samples

class Menu: #Start class Menu
    """
    This class manages the main user interface and navigation for the Sampling project.
    It provides nested menus for recording samples, editing audio, managing audio banks,
    and accessing different play modes like finger drumming and step sequencing.
    """

    def __init__(self): #Init contructor for Menu
        """
        Initializes the Menu instance, clears the console, and displays the main 
        welcome screen with high-level navigation options.
        """

        console = Console() #Create console object from rich library

        print("Menu initialized") #Work check

        #sleep(1) #Sleep 1 second
        console.clear() #Clear the terminal screen

        title = r"""

        ███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗ 
        ██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██║████╗  ██║██╔════╝ 
        ███████╗███████║██╔████╔██║██████╔╝██║     ██║██╔██╗ ██║██║  ███╗
        ╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██║██║╚██╗██║██║   ██║
        ███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗██║██║ ╚████║╚██████╔╝
        ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

        """ #Title ascii art

        console.rule(title = "Welcome to: ", characters = "=") #Print rule with rich library
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        console.rule(title = "By: Calak de Astora", characters = "=") #Print rule with rich library
        #print("\n\tWelcome to Sampling Proyect") #Welcome message

        #Print select option message
        console.print("\nSelect an option:", style="bold", justify = "center")
        console.print("1. Sample Menu", style = "bold magenta", justify = "full") #Print option 1
        #Print option 2
        console.print("2. Audio Bank Menu", style = "bold magenta", justify = "full")
        console.print("0. Exit", style = "bold red", justify = "full") #Print option 3

    #End contructor

    def menu_controls(self, option): #Start function menucontrols with option parameter
        """
        Processes the user's selection from the main menu and navigates to either 
        the Sample Menu, the Audio Bank Menu, or exits the application.
        """

        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            print("Sample Menu selected") #Print sample menu selected message
            console.clear() #Clear the terminal screen

            title = r"""

███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
███████╗███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██╗
███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝

            """ #Title ascii art

            #Print rule with rich library
            console.rule(title = "You are in: Sampler Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Main Menu", characters = "=")

            #Print select option message
            console.print("\nSelect an option:", style="bold", justify = "center")
            #Print option 1
            console.print("1. Record Mic Sample", style = "bold purple", justify = "full")
            #Print option 2
            console.print("2. Record Desk Sample", style = "bold purple", justify = "full")
            console.print("3. Easy Chop", style = "bold blue", justify = "full") #Print option 3
            console.print("4. Audio effects to sample", style = "bold green", justify = "full")
            console.print("0. Back", style = "bold yellow", justify = "full") #Print option 3

            #Input new option number
            new_option = int(console.input("\n[bold]Enter option number:[/bold] "))
            self.menu_sample(new_option) #Call MenuSample function with new option parameter

        elif option == 2: #Else if option is 2

            print("AudioBank Menu selected") #Print sample menu selected message
            console.clear() #Clear the terminal screen

            title = r"""

██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝
██████╔╝███████║██╔██╗ ██║█████╔╝ ███████╗
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ╚════██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: Banks Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Main Menu", characters = "=")

            #Print select option message
            console.print("\nSelect an option:", style="bold", justify = "full")
            console.print("1. Create Bank", style="bold white", justify = "full") #Print option 1
            console.print("2. Load Bank", style="bold blue", justify = "full") #Print option 2
            console.print("0. Back", style="bold yellow", justify = "full") #Print option 3

            #Input new option number
            new_option = int(console.input("\n[bold]Enter option number:[/bold] "))
            self.menu_bank(new_option) #Call MenuBank function with new option parameter

        elif option == 0: #Else if option is 0

            print("Exiting...") #Print exiting message
            sleep(1) #Sleep 1 second
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            exit() #Exit the program

        else: #Else

            print("Invalid option") #Print invalid option message

            #Input new option number
            new_option = int(console.input("\n[bold]Enter option number:[/bold] "))
            #Call menucontrols function again with new option parameter
            self.menu_controls(new_option)

    #End MenuControls

    def menu_sample(self, option): #Start function menusample with option parameter
        """
        Handles the logic for the Sample Menu, allowing users to record from 
        microphone/desktop, chop existing samples, or access the audio effects submenu.
        """

        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            print("Record Mic Sample selected") #Print record sample selected message
            console.clear() #Clear the terminal screen

            title = r"""

██████╗ ███████╗ ██████╗███╗   ███╗██╗ ██████╗██╗
██╔══██╗██╔════╝██╔════╝████╗ ████║██║██╔════╝██║
██████╔╝█████╗  ██║     ██╔████╔██║██║██║     ██║
██╔══██╗██╔══╝  ██║     ██║╚██╔╝██║██║██║     ╚═╝
██║  ██║███████╗╚██████╗██║ ╚═╝ ██║██║╚██████╗██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: RecMic Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Sampler Menu", characters = "=")

            option = int(console.input("\n[bold]Select time rec: [/bold]")) #Input option number
            #Call RecMic function from RecordSamp module with duration parameter
            rs.RecordSamp.rec_mic(duration=option)

            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_controls(1)

        elif option == 2: #Else if option is 2

            print("Record Desktop Sample selected") #Print record sample selected message
            console.clear() #Clear the terminal screen

            title = r"""

██████╗ ███████╗ ██████╗██████╗ ███████╗███████╗██╗  ██╗██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝██║
██████╔╝█████╗  ██║     ██║  ██║█████╗  ███████╗█████╔╝ ██║
██╔══██╗██╔══╝  ██║     ██║  ██║██╔══╝  ╚════██║██╔═██╗ ╚═╝
██║  ██║███████╗╚██████╗██████╔╝███████╗███████║██║  ██╗██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: RecDesk Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Sampler Menu", characters = "=")

            print("WIP Coming soon...") #Print coming soon message
            sleep(3) #Sleep 3 seconds

            #Input option number
            #option = int(input("\nSelect time rec: "))
            #Call RecMic function from RecordSamp module with duration parameter
            #rs.RecordSamp.RecDesk(duration=option)

            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_controls(1)

        elif option == 3: #Else if option is 3

            edit_sample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Chop Sample selected") #Print chop sample selected messages
            console.clear() #Clear the terminal screen

            title = r"""

███████╗███████╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ██╗
██╔════╝╚══███╔╝██╔════╝██║  ██║██╔═══██╗██╔══██╗██║
█████╗    ███╔╝ ██║     ███████║██║   ██║██████╔╝██║
██╔══╝   ███╔╝  ██║     ██╔══██║██║   ██║██╔═══╝ ╚═╝
███████╗███████╗╚██████╗██║  ██║╚██████╔╝██║     ██╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ 

            """

            #Print rule with rich library
            console.rule(title = "You are in: EasyChop Menu", characters = "=")
            #Print title with rich style
            console.print(title, style = "bold blue", justify = "center")
            #Print rule with rich library
            console.rule(title = "Back to: Sampler Menu", characters = "=")

            #Input option number
            option = int(console.input("\n[bold]Select number of slices: [/bold]"))
            edit_sample.ez_chop(num_slices=option) #Call Chop function from Record
            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_controls(1)

        elif option == 4: #Else if option is 4

            print("Audio effects to sample Menu") #Print audio effects to sample selected message
            console.clear() #Clear the terminal screen

            title = r"""

███████╗███████╗███████╗███████╗ ██████╗████████╗███████╗
██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝
█████╗  █████╗  █████╗  █████╗  ██║        ██║   ███████╗
██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  ██║        ██║   ╚════██║
███████╗██║     ██║     ███████╗╚██████╗   ██║   ███████║
╚══════╝╚═╝     ╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: Effects SubMenu", characters = "=")
             #Print title with rich style
            console.print(title, style = "bold blue", justify = "center")
            #Print rule with rich library
            console.rule(title = "Back to: Sampler Menu", characters = "=")

            #Print select option message
            console.print("\nSelect an option:", style="bold", justify = "center")
            console.print("1. Pass Filter", style="bold black", justify = "full") #Print option 1
            console.print("2. Pitch Control", style="bold green", justify = "full") #Print option 2
            console.print("0. Back", style="bold yellow", justify = "full") #Print option 3

            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.effects_sub_menu(option) #Call EffectsSubMenu function with option parameter
            #Call MenuSample function with option 4 parameter
            #to show audio effects to sample menu again
            self.menu_sample(4)

        elif option == 0: #Else if option is 0

            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.menu_controls(new_option) #Call menucontrols function with new option parameter

        else: #Else

            print("Invalid option") #Print invalid option message

            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.menu_sample(new_option) #Call menusample function again with new option parameter

    #End MenuSample

    def effects_sub_menu(self, option): #Start function effectsubmenu with option parameter
        """
        Manages the audio effects submenu, providing options for applying filters 
        or pitch control to selected audio samples.
        """

        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            edit_sample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Filter Sample selected") #Print filter sample selected message
            console.clear() #Clear the terminal screen

            title = r"""

██╗  ██╗██████╗ ██╗    ██╗██╗     ██████╗ ██╗
██║  ██║██╔══██╗██║   ██╔╝██║     ██╔══██╗██║
███████║██████╔╝██║  ██╔╝ ██║     ██████╔╝██║
██╔══██║██╔═══╝ ╚═╝ ██╔╝  ██║     ██╔═══╝ ╚═╝
██║  ██║██║     ██╗██╔╝   ███████╗██║     ██╗
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    ╚══════╝╚═╝     ╚═╝ 

            """

            #Print rule with rich library
            console.rule(title = "You are in: Filter Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Effects SubMenu", characters = "=")

            #Call Catch function from EditSamp object with True
            # parameter to indicate it was called from the main menu
            edit_sample.catch(True)

            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_sample(4)

        elif option == 2: #if option is 2

            edit_sample = es.EditSamp() #Create object EditSample from EditSamp module

            print("Pitch Control selected") #Print pitch control selected message
            console.clear() #Clear the terminal screen

            title = r"""

██████╗ ██╗████████╗ ██████╗██╗  ██╗██╗
██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║██║
██████╔╝██║   ██║   ██║     ███████║██║
██╔═══╝ ██║   ██║   ██║     ██╔══██║╚═╝
██║     ██║   ██║   ╚██████╗██║  ██║██╗
╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: Pitch Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Effects SubMenu", characters = "=")

            #Call PitchControl function from EditSamp object
            #with False parameter to indicate it was called from the main menu
            edit_sample.catch(False)

            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_sample(4)

        elif option == 0: #Else if option is 0

            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            #Call menucontrols function with option 1 parameter to show sample menu again
            self.menu_controls(1)

        else: #Else

            print("Invalid option") #Print invalid option message
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.effects_sub_menu(new_option) #Call EffectsSubMenu function again with new option

    #End EffectsSubMenu

    def menu_bank(self, option): #Start function menubank with option parameter
        """
        Coordinates the Audio Bank Menu, enabling users to create new sound banks, 
        load existing configurations, and subsequently enter the Play Menu.
        """

        global backopt #Global variable to control back option in play menu
        backopt = 1 #Set backopt to 1 to control back option in play

        audio_bank = ab.AudioBank() #Create object AudioBank from AudioBank module
        console = Console() #Create console object from rich library

        if option == 1: #If option is 1

            print("\tCreate Bank") #Print create bank selected message
            console.clear() #Clear the terminal screen

            title = r"""

 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ╚═╝
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝

            """

            #Print rule with rich library
            console.rule(title = "You are in: Bank Create Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Banks Menu", characters = "=")

            #Call CreateBank function from AudioBank object and saves the returned sounds
            sound = audio_bank.create_bank()

            #If sound is None it means that the user canceled the
            #bank creation process and we need to go back to the bank menu
            if sound == None:

                #Print cancel message
                console.print("" \
                "\nBank creation canceled, going back to Banks Menu...",
                style="bold red", justify="center"
                )
                sleep(1) #Sleep 3 seconds
                #Call MenuBank function with option 2 parameter to show bank menu again
                self.menu_controls(2)

            self.show_play_menu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.play_menu(option, sound) #Call PlayMenu function with option parameter

        elif option == 2: #Else if option is 2

            print("\tLoad Bank") #Print load bank selected message
            console.clear() #Clear the terminal screen

            title = r"""

██╗      ██████╗  █████╗ ██████╗ 
██║     ██╔═══██╗██╔══██╗██╔══██╗
██║     ██║   ██║███████║██║  ██║
██║     ██║   ██║██╔══██║██║  ██║
███████╗╚██████╔╝██║  ██║██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

            """

            #Print rule with rich library
            console.rule(title = "You are in: Bank Load Menu", characters = "=")
            console.print(title, style="bold blue", justify="center") #Print title with rich style
            #Print rule with rich library
            console.rule(title = "Back to: Banks Menu", characters = "=")

            sound = audio_bank.load_bank() #Call LoadBank function from AudioBank object

            #If sound is None it means that the user canceled the bank
            #creation process and we need to go back to the bank menu
            if sound == None:

                #Print cancel message
                console.print(
                    "\nBank Load canceled, going back to Banks Menu...",
                    style="bold red", justify="center"
                    )
                sleep(1) #Sleep 3 seconds
                #Call MenuBank function with option 2 parameter to show bank menu again
                self.menu_controls(2)

            self.show_play_menu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.play_menu(option, sound) #Call PlayMenu function with option parameter

        elif option == 0: #Else if option is 0

            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            #Input new option number
            new_option = int(console.input("\n[bold]Enter option number: [/bold]"))
            self.menu_controls(new_option) #Call menucontrols function with new option parameter

        else: #Else

            print("Invalid option") #Print invalid option message

            #Input new option number
            new_option = int(console.input("\n[bold]Enter option number: [/bold]"))
            self.menu_bank(new_option) #Call menubank function again with new option parameter

    #End MenuBank

    def show_play_menu(self): #Start function playmenu
        """
        Displays the available play modes (Finger Drumming or Step Sequencer) 
        after an audio bank has been successfully created or loaded.
        """

        console = Console() #Create console object from rich library

        print("\tPlay Menu") #Print play menu message
        console.clear() #Clear the terminal screen

        title = r"""

██████╗ ██╗      █████╗ ██╗   ██╗██╗████████╗██╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║╚══██╔══╝██║
██████╔╝██║     ███████║ ╚████╔╝ ██║   ██║   ██║
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║   ██║   ╚═╝
██║     ███████╗██║  ██║   ██║   ██║   ██║   ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝

            """

        #Print rule with rich library
        console.rule(title = "You are in: Play Menu", characters = "=")
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        #Print rule with rich library
        console.rule(title = "Back to: Banks Menu", characters = "=")

        #Print select option message
        console.print("\nSelect an option:", style="bold", justify="center")
        console.print("1. Finger Drumming", style="bold white", justify="full") #Print option 1
        console.print("2. Step Seq", style="bold blue", justify="full") #Print option 2
        console.print("0. Back", style="bold yellow", justify="full") #Print option 3

    #End ShowPlayMenu

    def play_menu(self, option, sound): #Start function playmenu with option and sound parameter
        """
        Executes the chosen play mode (Finger Drumming or Step Sequencer) using 
        the provided sound bank data and handles returning to previous menus.
        """

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        play_modes = pm.PlayModes() #Create object PlayModes from PlayMode module
        console = Console() #Create console object from rich library

        if option == 1:#If option is 1:

            #Call FingerDrum function from PlayModes object with sound parameter
            play_modes.finger_drum(sound)

            self.show_play_menu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.play_menu(option, sound) #Call PlayMenu function with option parameter

        elif option == 2:

            #Call StepSeq function from PlayModes object with sound parameter
            play_modes.step_seq(sound)

            self.show_play_menu() #Call ShowPlayMenu function
            option = int(console.input("\n[bold]Enter option number: [/bold]")) #Input option number
            self.play_menu(option, sound) #Call PlayMenu function with option parameter

        elif option == 0: #Else if option is 0

            print("Backing...") #Print progress message
            #sleep(1) #Sleep 1 second

            if backopt == 1:

                #Call menucontrols function with option 2 parameter to show audio bank menu again
                self.menu_controls(2)
                #Input new option number
                new_option = int(input("\n[bold]Enter option number: [/bold]"))
                self.menu_bank(new_option) #Call MenuBank function with new option parameter

            elif backopt == 0:

                #Call menucontrols function with option 2 parameter to show audio bank menu again
                self.menu_controls(1)
                #Input new option number
                new_option = int(input("\n[bold]Enter option number: [/bold]"))
                self.menu_bank(new_option) #Call MenuBank function with new option parameter

        else:

            print("Invalid option") #Print invalid option message

            new_option = int(input("\n[bold]Enter option number: [/bold]")) #Input new option number
            self.menu_bank(new_option) #Call menubank function again with new option parameter

    #End PlayMenu

#End class Menu
