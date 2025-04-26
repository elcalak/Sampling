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
Compile in environment (in Arch): Environment/piplibs/bin/python
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk

"""

import os #Call the module os to control path files 
import tkinter as tk #Call the module Tkinter as tk to control file dialogs
from tkinter import filedialog #From the module Tkinter call the metoth filedialog
import json #Call the module json to save config files

class AudioBank: #Start class Audio bank

    DEFAULT_BANK_PATH = "/home/elcalak/Repositorys/elcalak/Sampling/AudioBanks/Default" #Set default path for default bank

    def __init__(self, name="DefaultBank"): #Init contructor to default bank

        self.name = name #Set the name "DefaultBank"
        self.base_path = AudioBank.DEFAULT_BANK_PATH #Set default bank path

        self._sounds = {} #Create a sound library 

        for i in range(1,10): #Init for to load the defualt audio files
            
            placeholder_path = os.path.join(self.base_path, f"slot{i}.wav") #Search the files in deafult path
            print(f"Hi im defualt slot{i}") #Work check
            self._sounds[i] = placeholder_path #Saves files in the sound library
        #End for
    
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
        
        #End contradiction

        self.sounds = {} #Create a sound library

        for i in range(1,10): #Init for to load the audio files

            self.sounds[i] = filedialog.askopenfile(title = f"Select slot{i}") #Select audio files to slot
            print(f"Hi im slot{i}") #Work check
        
        #End for to load files

    #End create bank function

    def SaveBank(self): # Function to save the bank configuration
    
        if not self.name or not self.base_path:
             print("Cannot save bank. Name or base path is missing.")
             print("Please create or load a bank first.")
             return

        root = tk.Tk()
        root.withdraw()

        # Prepare data to save
        bank_data = {
            "name": self.name,
            "base_path": self.base_path,
            "sounds": self.sounds
        }

        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(
            title=f"Save Bank Configuration '{self.name}'",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=f"{self.name}_bank.json" # Suggest a filename
        )

        root.destroy() # Clean up Tk instance

        if file_path:
            try:
                with open(file_path, 'w') as f:
                    json.dump(bank_data, f, indent=4) # Use indent for readability
                print(f"Bank '{self.name}' saved successfully to: {file_path}")
            except IOError as e:
                print(f"Error saving bank configuration: {e}")
            except Exception as e:
                 print(f"An unexpected error occurred during saving: {e}")
        else:
            print("Save operation cancelled.")

    # End SaveBank function

    def LoadBank(self):

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Load Bank Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        root.destroy()

        if file_path:
            try:
                with open(file_path, 'r') as f:
                    bank_data = json.load(f)

                # Validate loaded data (basic check)
                if "name" in bank_data and "base_path" in bank_data and "sounds" in bank_data:
                    self.name = bank_data["name"]
                    self.base_path = bank_data["base_path"]
                    # Convert keys back to integers if needed (JSON saves keys as strings)
                    self.sounds = {int(k): v for k, v in bank_data["sounds"].items()}
                    print(f"Bank '{self.name}' loaded successfully from: {file_path}")
                else:
                    print("Error: Invalid bank configuration file format.")

            except FileNotFoundError:
                print(f"Error: File not found - {file_path}")
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from file - {file_path}")
            except IOError as e:
                print(f"Error reading bank configuration file: {e}")
            except Exception as e:
                 print(f"An unexpected error occurred during loading: {e}")
        else:
            print("Load operation cancelled.")

#End AudioBank class

Bank1 = AudioBank()

Bank1.CreateBank()
Bank1.SaveBank()