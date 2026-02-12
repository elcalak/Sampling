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

class Menu: #Start class Menu

    def __init__(self): #Init contructor for Menu

        print("Menu initialized") #Work check
        
        sleep(1) #Sleep 1 second
        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen

        print("\n\tWelcome to Sampling Proyect") #Welcome message
        
        print("\nSelect an option:") #Print select option message
        print("1. Sample Menu") #Print option 1
        print("2. Audio Bank Menu") #Print option 2
        print("0. Exit") #Print option 3

    #End contructor

    def MenuControls(self, option): #Start function menucontrols with option parameter

        if option == 1: #If option is 1
            
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("Sample Menu selected") #Print sample menu selected message
            print("\nSelect an option:") #Print select option message
            print("1. Record Mic Sample") #Print option 1
            print("2. Record Desk Sample") #Print option 2
            print("0. Back") #Print option 3
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuSample(new_option) #Call MenuSample function with new option parameter
            
        elif option == 2: #Else if option is 2
            
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("AudioBank Menu selected") #Print sample menu selected message
            print("\nSelect an option:") #Print select option message
            print("1. Create Bank") #Print option 1
            print("2. Load Bank") #Print option 2
            print("0. Back") #Print option 3
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuBank(new_option) #Call MenuBank function with new option parameter

        elif option == 0: #Else if option is 0
            
            print("Exiting...") #Print exiting message
            sleep(1) #Sleep 1 second
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            exit() #Exit the program

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function again with new option parameter

    #End MenuControls

    def MenuSample(self, option): #Start function menusample with option parameter

        if option == 1: #If option is 1
            
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("Record Mic Sample selected") #Print record sample selected message

            option = int(input("\nSelect time rec: ")) #Input option number
            rs.RecordSamp.RecMic(duration=option) #Call RecMic function from RecordSamp module with duration parameter

            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again

        elif option == 2: #Else if option is 2
            
            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("Record Mic Sample selected") #Print record sample selected message

            option = int(input("\nSelect time rec: ")) #Input option number
            rs.RecordSamp.RecDesk(duration=option) #Call RecMic function from RecordSamp module with duration parameter

            self.MenuControls(1) #Call menucontrols function with option 1 parameter to show sample menu again

        elif option == 0: #Else if option is 3
            
            print("Backing...") #Print progress message
            sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function with new option parameter

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuSample(new_option) #Call menusample function again with new option parameter

    def MenuBank(self, option): #Start function menubank with option parameter
        
        global backopt #Global variable to control back option in play menu
        backopt = 1 #Set backopt to 1 to control back option in play

        if option == 1: #If option is 1
            
            AudioBank = ab.AudioBank() #Create object AudioBank from AudioBank module

            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("\tCreate Bank") #Print create bank selected message
            
            sound = AudioBank.CreateBank() #Call CreateBank function from AudioBank object and saves the returned sounds
            
            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(input("\nEnter option number: ")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter

        elif option == 2: #Else if option is 2
            
            AudioBank = ab.AudioBank() #Create object AudioBank from AudioBank module

            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
            print("\tLoad Bank") #Print load bank selected message
            
            sound = AudioBank.LoadBank() #Call LoadBank function from AudioBank object

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(input("\nEnter option number: ")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter

        elif option == 0: #Else if option is 3
        
            print("Backing...") #Print progress message
            sleep(1) #Sleep 1 second
            self.__init__() #Call init constructor to show main menu again

            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuControls(new_option) #Call menucontrols function with new option parameter

        else: #Else
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuBank(new_option) #Call menubank function again with new option parameter

    #End MenuBank

    def ShowPlayMenu(self): #Start function playmenu

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        print("\tPlay Menu") #Print play menu message
        print("\nSelect an option:") #Print select option message
        print("1. Finger Drumming") #Print option 1
        print("2. Step Seq") #Print option 2
        print("0. Back") #Print option 3

    #End ShowPlayMenu

    def PlayMenu(self, option, sound): #Start function playmenu with option and sound parameter

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        PlayMode = pm.PlayModes() #Create object PlayModes from PlayMode module

        if option == 1:#If option is 1:
        
            PlayMode.FingerDrum(sound) #Call FingerDrum function from PlayModes object with sound parameter

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(input("\nEnter option number: ")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter
            
        elif option == 2:
            
            PlayMode.StepSeq(sound) #Call StepSeq function from PlayModes object with sound parameter

            self.ShowPlayMenu() #Call ShowPlayMenu function
            option = int(input("\nEnter option number: ")) #Input option number
            self.PlayMenu(option, sound) #Call PlayMenu function with option parameter
        
        elif option == 0: #Else if option is 0
            
            print("Backing...") #Print progress message
            sleep(1) #Sleep 1 second
            
            if backopt == 1:

                self.MenuControls(2) #Call menucontrols function with option 2 parameter to show audio bank menu again
                new_option = int(input("\nEnter option number: ")) #Input new option number
                self.MenuBank(new_option) #Call MenuBank function with new option parameter
            
            elif backopt == 0:
                
                self.MenuControls(1) #Call menucontrols function with option 2 parameter to show audio bank menu again
                new_option = int(input("\nEnter option number: ")) #Input new option number
                self.MenuBank(new_option) #Call MenuBank function with new option parameter

        else:
            
            print("Invalid option") #Print invalid option message
            
            new_option = int(input("\nEnter option number: ")) #Input new option number
            self.MenuBank(new_option) #Call menubank function again with new option parameter

    #End PlayMenu

#End class Menu

#These work chek lines go to the Main file (Maybe):

Menu = Menu() #Create object Menu

opti = int(input("\nEnter option number: ")) #Input option number

Menu.MenuControls(opti) #Call menucontrols function with option parameter

#End work chek lines