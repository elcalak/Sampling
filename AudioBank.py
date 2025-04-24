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

"""

import os #Call the module os to control path files 
import tkinter as tk
from tkinter import filedialog

class AudioBank: #Start class Audio bank

    DEFAULT_BANK_PATH = "/home/elcalak/Repositorys/elcalak/Sampling/AudioBanks/Default" #Set default path for default bank

    def __init__(self, name="DefaultBank"): #Init contructor to default bank

        self.name = name #Set the name "DefaultBank"
        self.base_path = AudioBank.DEFAULT_BANK_PATH #Set default bank path

        self._sounds = {} #Create a sound library 

        for i in range(1,10): #Init for to load the defualt audio files
            
            placeholder_path = os.path.join(self.base_path, f"slot{i}.wav") #Search the files in deafult path
            print(f"Hi im slot{i}") #Work check
            self._sounds[i] = placeholder_path #Saves files in the sound library
        #End for
    
    #End constructor

    def CreateBak(): #Function to create a new bank

        root = tk.Tk() #Create a Tk object
        root.withdraw() #Hide the main dialog

        BankName = input("Select bank name: ") #Ask user to name for bank

        Bank.name = BankName #Set the name assigned
        Bank.base_path = filedialog.askdirectory(title = "Select folder",) #Set the base path from bank

        tk.Tk().destroy() #Close root dialog

        if Bank.base_path: #Verify slection
            
            print(f"Folder select: {Bank.base_path}") #Print Succes path select

        else: #Contradiction

            print("No folder select.") #Print error message
        
        for i in range(1,10): #Init for to load the audio files

            Bank.sounds[i] = filedialog.askopenfile(title = f"Select slot{i}") #Select audio files to slot
            print(f"Hi im slot{i}") #Work check