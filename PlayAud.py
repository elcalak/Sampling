"""

This file controls the audio reproduction

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

import simpleaudio as sa #Module to control Wavfiles
import pygame as pg
import time

def playwav(file): #Function play for wav files

    try: #Init try

        wave_obj = sa.WaveObject.from_wave_file(file) #Create a wave object from a wave file
        play = wave_obj.play() #Play the wave object
        return play, wave_obj, #print("Im playwav fun!") #Line for work chek #Returns play and wave object
    #Finish Try
    
    except FileNotFoundError: #Init except
        
        print(f"¡Oops! No encontré el archivo: {filename}") #Print error message
        return None, NoneActive #Return none
    #Finish Except

def playmp3(file): #Function play for mp3 files

    try: #Init try
        
        pg.mixer.init() #Start module mixer from pygame
        pg.mixer.music.load(file) #Load MP3
        pg.mixer.music.play() #Start play
        return pg.mixer.music, True, #print("Im playmp3 fun!") #Line for work check #Return pygame mixer
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

file = '/home/elcalak/Downloads/Angustia.wav'
playwav(file)