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

import pygame as pg
from time import sleep

def play(file): #Function play for mp3 files

    try: #Init try
        
        print("Hi im a try!")

        pg.mixer.init() #Start module mixer from pygame
        global sound
        print("Hey im initi the mixer!") #Line for work check

        if file.endswith(".mp3") or file.endswith(".ogg"): #Start condicional for compress format
            
            sound = pg.mixer.music.load(file) #Load MP3
            sound.mixer.music.play() #Start play
            print("Im playmp3 fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for compress formats

        elif file.endswith(".wav"): #Start condicional for wav format
            
            sound = pg.mixer.Sound(file) #Load WAV
            sound.play() #Start play
            print("Im playwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

        else: #Start the last condicional 

            print("No supported format") #Print error menssage for no supported formats
        #Finish condicional
       
    #Finish Try 
    
    except pygame.error as e: #Init except
    
        print(f"¡Oops! Ocurrió un error al cargar o reproducir el archivo: {file}") #Print error message
        print(f"Error de Pygame: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

    except FileNotFoundError: #Init except
        
        print(f"¡Oops! No encontré el archivo: {file}") #Print error message
        return None, False #Return none and false
    #Finish Except

print("Im alavie")
file = '/home/elcalak/Downloads/Angustia.wav'
play(file)
