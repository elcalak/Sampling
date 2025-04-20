"""

This file controls the audio recording for the Sampling proyect

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

from time import sleep #From module time import sleep function
import sounddevice as sd #Call the module sounddevice as sd for record audio
import numpy as np #Call numpy for control of audio arrays
from scipy.io.wavfile import write #Call function write from the module scipy
import os #Call the module os to control path files 
import datetime #Call the module datetime to control date

def RecMic(duration=5, fs=44100): #Function Record microphone

    print(f"Starting record of {duration} seconds...") #Print start record message

    try: #Init try
    
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16') #Rec microphone on stereo
        sd.wait()  #Wait to rec finish

        output_dir = "Records" #Define the folder save name

        if not os.path.exists(output_dir): #Start conditional to create directory
            os.makedirs(output_dir) #Create directory
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #Generate timestamp
        filename = f"recording_{timestamp}.wav" #Create unique filename

        filepath = os.path.join(output_dir, filename) #Define save path and save name
        
        write(filepath, fs, recording)  #Save file

        print(f"Rec saved in: {filepath}") #Print finish record message and the file path

        return filepath #Returns file path

    #Finish try

    except Exception as e: #Init except
        
        print(f"Rec error: {e}") #Print error message
        print("Your mic works on?.") #Print first suggest
        print("Verify the sound devices:") #Print second suggest
        print("python -m sounddevice") #Print verify instructions
        
        return None #Returns none
    
    #Init except

"""
def RecDesk(duration=5, fs=44100, channel = 2): #Function Record Desktop

    print(f"Starting record of {duration} seconds...") #Print start record message

    try: #Init try
    
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=channel, dtype='int16', device='Bocina Selfie-82') #Rec desktop on stereo
        sd.wait()  #Wait to rec finish

        output_dir = "Record desktop" #Define the folder save name

        if not os.path.exists(output_dir): #Start conditional to create directory
            os.makedirs(output_dir) #Create directory
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #Generate timestamp
        filename = f"recording_{timestamp}.wav" #Create unique filename

        filepath = os.path.join(output_dir, filename) #Define save path and save name
        
        write(filepath, fs, recording)  #Save file

        print(f"Rec saved in: {filepath}") #Print finish record message and the file path

        return filepath #Returns file path

    #Finish try

    except Exception as e: #Init except
        
        print(f"Rec error: {e}") #Print error message
        print("Your devices is correctly?.") #Print first suggest
        print("Verify the sound devices:") #Print second suggest
        print("python -m sounddevice") #Print verify instructions
        
        return None #Returns none
    
    #Init except
"""

#RecMic()