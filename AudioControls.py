"""

This file controls the audio reproduction for the Sampling proyect

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

import pygame as pg #Call the module pygame as pg
from time import sleep #From module time import sleep function

def load(file): #Function load files
    
    global sound #Global variable sound to save the current audio
    print("Im load fun!") #Line for work check

    try: #Init try
        
        print("Hi im load try!") #Line for work check

        pg.mixer.init() #Start module mixer from pygame
        print("Hey im starting the mixer!") #Line for work check

        if file.endswith(".mp3") or file.endswith(".ogg"): #Start condicional for compress format
            
            sound = pg.mixer.music.load(file) #Load MP3
            print("Im loadmp3 fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for compress formats

        elif file.endswith(".wav"): #Start condicional for wav format
            
            sound = pg.mixer.Sound(file) #Load WAV
            print("Im loadwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

        else: #Start the last condicional 

            print("No supported format") #Print error menssage for no supported formats
        #Finish condicional
       
    #Finish Try 
    
    except pygame.error as e: #Init except
    
        print(f"Error to load or play the file: {file}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

    except FileNotFoundError: #Init except
        
        print(f"File: {file} not found") #Print error message
        return None, False #Return none and false
    #Finish Except

def play(): #Function play

    print("Im play fun!") #Line for work check

    try: #Init try
        
        print("Hi im play try!") #Line for work check

        if sound == None: #Start condicional for compress format
            
            sound.mixer.music.play() #Start play
            print("Im playmp3 fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format
            
            sound.play() #Start play
            print("Im playwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format
       
    #Finish Try 
    
    except pygame.error as e: #Init except
    
        print(f"Error to load or play the file: {file}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

def stop():
    
    print("Im stop fun!") #Line for work check

    try: #Init try
        
        print("Hi im a try!") #Line for work check

        if sound == None: #Start condicional for compress format
            
            sound.mixer.music.stop() #Stop play
            print("Im stopmp3 fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format

            sound.stop() #Stop play
            print("Im stopwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

    #Finish Try 
    
    except pygame.error as e: #Init except
    
        print(f"Error to load or play the file: {file}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

print("Im alavie")
archivo = '/home/elcalak/Downloads/Angustia.wav'
load(archivo)
play()
sleep(5)
stop()