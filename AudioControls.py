"""

This file controls the audio for the Sampling proyect

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

import pygame as pg #Call the module pygame as pg to playing audio
from time import sleep #From module time import sleep function

def load(file): #Function load files
    
    global sound, file_type #Global variable sound to save the current audio
    print("Im load fun!") #Line for work check

    try: #Init try
        
        print("Hi im load try!") #Line for work check

        pg.mixer.init() #Start module mixer from pygame
        print("Hey im starting the mixer!") #Line for work check

        if file.endswith(".mp3") or file.endswith(".ogg"): #Start condicional for compress format
            
            pg.mixer.music.load(file) #Load MP3
            print("Im loadmp3 fun!") #Line for work check
            file_type = "mp3"
            return pg.mixer.music, True #Return pygame mixer
        #Finish condicional for compress formats

        elif file.endswith(".wav"): #Start condicional for wav format
            
            sound = pg.mixer.Sound(file) #Load WAV
            print("Im loadwav fun!") #Line for work check
            file_type = "wav"
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

        else: #Start the last condicional 

            print("No supported format") #Print error menssage for no supported formats
        #Finish condicional
       
    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Error to load or play the file: {file}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

    except FileNotFoundError: #Init except
        
        print(f"File: {file} not found") #Print error message
        return None, False #Return none and false
    #Finish Except

#End Function load

def play(): #Function play

    print("Im play fun!") #Line for work check
    global song_status

    try: #Init try
        
        print("Hi im play try!") #Line for work check

        if file_type == "mp3": #Start condicional for compress format
            
            pg.mixer.music.play() #Start play
            print("Im playmp3 fun!") #Line for work check
            song_status = True
            return pg.mixer.music, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format
            
            global status_sound #Global variable playsound to save the current status of sound
            status_sound = sound.play() #Start play
            print("Im playwav fun!") #Line for work check
            song_status = False
            return sound, True #Return pygame mixer
        #Finish condicional for wav format
       
    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

#End Function play

def pause(): #Function pause

    print("Im pause fun!") #Line for work check

    try: #Init try
        
        print("Hi im pause try!") #Line for work check

        if song_status == True or status_sound.get_busy() == True: #Start condicional know if music is played
        
            if file_type == "mp3": #Start condicional for compress format
            
                pg.mixer.music.pause() #Start pause
                print("Im pausemp3 fun!") #Line for work check
                return pg.mixer.music, True #Return pygame mixer
            #Finish condicional for compress formats

            else: #Start condicional for wav format
            
                status_sound.pause() #Start pause
                print("Im pausewav fun!") #Line for work check
                return sound, True #Return pygame mixer
            #Finish condicional for wav format
       
       #Finish conditional for know music status
        else:
    
            print("No music are play") #Error message
    
    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

#Finish Function pause

def resume(): #Function resume

    print("Im resume fun!") #Line for work check

    try: #Init try
        
        print("Hi im resume try!") #Line for work check

        if song_status == True or status_sound.get_busy() == True: #Start condicional know if music is played
        
            if file_type == "mp3": #Start condicional for compress format
            
                pg.mixer.music.unpause() #Start resume
                print("Im resumemp3 fun!") #Line for work check
                return pg.mixer.music, True #Return pygame mixer
            #Finish condicional for compress formats

            else: #Start condicional for wav format
            
                status_sound.unpause() #Start resume
                print("Im resumewav fun!") #Line for work check
                return sound, True #Return pygame mixer
            #Finish condicional for wav format
       
       #Finish conditional for know music status
        else:
    
            print("No music are play") #Error message
    
    #Finish Try 
    
    except pg.error as e: #Init except

        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

#Finish Function resume

def stop(): #Function stop
    
    print("Im stop fun!") #Line for work check

    try: #Init try
        
        print("Hi im a stop try!") #Line for work check

        if file_type == "mp3": #Start condicional for compress format
            
            pg.mixer.music.stop() #Stop play
            print("Im stopmp3 fun!") #Line for work check
            return pg.mixer.music, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format

            sound.stop() #Stop play
            print("Im stopwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Error to load or play the file: {file}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none add false
    #Finish Except

#End Function stop

""" Function checks:

print("Im alavie")
archivo = '/home/elcalak/Repositorys/elcalak/Sampling/Records/recording_20250418_190024.wav'
load(archivo)
play()
sleep(5)
pause()
sleep(5)
resume()
sleep(5)
stop()

"""