"""

This file controls the Audio banks for the Sampling proyect

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

import os #Call the module os to control path files 
import tkinter as tk #Call the module Tkinter as tk to control file dialogs
from tkinter import filedialog #From the module Tkinter call the metoth filedialog
import json #Call the module json to save config files
import AudioControls as ac #Call the objects from AudioControl

class AudioBank: #Start class Audio bank

    DEFAULT_BANK_PATH = "$HOME/Sampling/AudioBanks/Default" #Set default path for default bank

    def __init__(self, name="DefaultBank"): #Init contructor to default bank

        self.name = name #Set the name "DefaultBank"
        self.base_path = AudioBank.DEFAULT_BANK_PATH #Set default bank path

        self._sounds = {} #Create a sound library 

        if self.base_path: #Verify path
        
            print(f"Default folder select: {self.base_path}") #Print Succes path select
        
        #End verify path

        else: #Contradiction
            
            print("No default folder select.") #Print error message
            return #Return to the main function
        
        #End contradiction

        for i in range(1,10): #Init for to load the defualt audio files
            
            file = os.path.join(self.base_path, f"slot{i}.wav") #Search the files in deafult path
            
            if file: #Verify if the file exist
            
                print(f"Hi im defualt slot{i}") #Work check
                self._sounds[i] = file #Saves files in the sound library

            #End verify if the file exist

            else: #Contradiction
                
                print(f"File not found: {file}") #Print error message
                return #Return to the main function
            
            #End contradiction

        #End for

        #print(self._sounds) #Work check

        ac.load(self._sounds) #Load the files in the AudioControl module

    #End constructor

    def CreateBank(self): #Function to create a new bank

        root = tk.Tk() #Create a Tk object
        root.withdraw() #Hide the main dialog

        BankName = input("Select bank name: ") #Ask user to name for bank

        self.name = BankName #Set the name assigned
        self.base_path = filedialog.askdirectory(title = "Select folder",) #Set the base path from bank

        tk.Tk().destroy() #Close root dialog

        if self.base_path: #Verify slection
            
            print(f"Folder select: {self.base_path}") #Print Succes path select

        #End verfify selection

        else: #Contradiction

            print("No folder select.") #Print error message
            return #Return to the main function
        
        #End contradiction

        self.sounds = {} #Create a sound library
        
        print("Select audio files for the bank:") #Print message to select audio files

        for i in range(1,10): #Init for to load the audio files

            file = filedialog.askopenfilename(title = f"Select slot{i}") #Select audio files to slot
            
            if file: #Verify if the file exist

                self.sounds[i] = file #Saves files in the sound library
                print(f"Hi im slot{i}") #Work check
        
            #End verify if the file exist
            
            else: #Contradiction

                print(f"File not found: {file}") #Print error message
                return #Return to the main function
            
            #End contradiction

        #End for to load files
        
        #ac.load(self.sounds) #Load the files in the AudioControl module
        
        print("Bank created successfully.") #Print succes message
        print("Do you want to save the bank configuration? (y/n)") #Ask user to save the bank configuration

        save_option = input().lower() #Input save option and convert to lowercase

        if save_option == 'y': #If user want to save the bank
            
            self.SaveBank() #Call SaveBank function

        elif save_option == 'n': #If user dont want to save the bank
            
            print("Bank not saved.") #Print message
        
        #End if save option
        
        return self.sounds
    #End create bank function

    def SaveBank(self): #Function to save the bank configuration
    
        if not self.name or not self.base_path: #Verify path and name from bank
             
             print("Cannot save bank. Name or base path is missing.") #Print error message
             print("Please create or load a bank first.") #Print suggest message
             
             return

        root = tk.Tk() #Create a Tk object
        root.withdraw() #Hide main dialog

        # Prepare data to save

        bank_data = { #Create a bank data list
            
            "name": self.name, #Name from bank
            "base_path": self.base_path, #Path from bank
            "sounds": self.sounds #Sound path from bank
        
        } #End list

        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename( #Open file dialog to chose name to save

            title=f"Save Bank Configuration '{self.name}'", #Title from Tk form
            defaultextension=".json", #Extension from archive
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")], #File type search
            initialfile=f"{self.name}_bank.json" #Suggest a filename
        
        ) #End dialog

        root.destroy() # Clean up Tk instance

        if file_path: #Verify path
            
            try: #Init try
            
                with open(file_path, 'w') as f: #Verify path
            
                    json.dump(bank_data, f, indent=4) #Use indent for readability
            
                print(f"Bank '{self.name}' saved successfully to: {file_path}") #Save file message
                #End with
            
            #End try

            except IOError as e: #Init except Input/output error
                
                print(f"Error saving bank configuration: {e}") #Print error message
            
            #End except

            except Exception as e: #Init except for unexcepted error
            
                 print(f"An unexpected error occurred during saving: {e}") #Print error message

            #End except
        
        else: #Contradiction
        
            print("Save operation cancelled.") #Print message
        
        #End else

    # End SaveBank function

    def LoadBank(self): #Function to load the bank configuration

        root = tk.Tk() #Create a Tk object
        root.withdraw() #Hide main dialog

        file_path = filedialog.askopenfilename( #Open file dialog to chose file
            
            title="Load Bank Configuration", #Title from Tk form
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")] #File type search
        
        ) #End dialog

        root.destroy() #Clean up Tk instance

        if file_path: #Verify path

            try: #Init try

                with open(file_path, 'r') as f: #Verify path
                
                    bank_data = json.load(f) #Load data

                # Validate loaded data (basic check)
                #End with
                
                if "name" in bank_data and "base_path" in bank_data and "sounds" in bank_data: #Verify data
                
                    self.name = bank_data["name"] #Load name bank

                    self.base_path = bank_data["base_path"] #Load bank path
                    
                    # Convert keys back to integers if needed (JSON saves keys as strings)
                    
                    self.sounds = {int(k): v for k, v in bank_data["sounds"].items()}
                
                    print(f"Bank '{self.name}' loaded successfully from: {file_path}") #Load file message
                
                    #ac.load(self.sounds) #Load the files in the AudioControl module
                
                #End load data

                else: #Contradiction
                
                    print("Error: Invalid bank configuration file format.") #Print error message

                #End contradiction

            except FileNotFoundError: #Init except for File not found
                
                print(f"Error: File not found - {file_path}") #Print error message
            
            #End except File not found

            except json.JSONDecodeError: #Init except JSON decode error
            
                print(f"Error: Could not decode JSON from file - {file_path}") #Print error message
            
            #End except JSON decode error

            except IOError as e: #Init except Input/output error
            
                print(f"Error reading bank configuration file: {e}") #Print error message
            
            #End except Input/output error

            except Exception as e: #Init except for unespected error
            
                 print(f"An unexpected error occurred during loading: {e}") #Print error message

            #End except unspected error

        else: #Contradiction
            
            print("Load operation cancelled.") #Print message
        
        #End contradiction

        return self.sounds

    #End LoadBank function

#End AudioBank class

#""" Work chek lines:

#Bank1 = AudioBank()

#Bank1.CreateBank()
#Bank1.SaveBank()

#""" End work check lines