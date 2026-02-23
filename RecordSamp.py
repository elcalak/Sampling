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
Compile in environment: Use Environment.sh to install all dependencies

"""

import sounddevice as sd #Call the module sounddevice as sd for record audio
import numpy as np #Call numpy for control of audio arrays
from scipy.io.wavfile import write #Call function write from the module scipy
import os #Call the module os to control path files 
import datetime #Call the module datetime to control date

class RecordSamp: #Start class RecordSamp

    def RecMic(duration, fs=44100): #Function Record microphone

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
    
        #Finish except

    #Finish function RecMic

#Finish class RecordSamp

    def RecDesk(duration, fs=44100, channel = 2): #Function Record Desktop

        try: #Init try
    
            devices = sd.query_devices() #Get all devices
            input_devices = [] #List to save input devices
            print("\nAvailable Input Devices:") #Print title
            print("0. Default Device") #Print default option

            for i, dev in enumerate(devices): #Iterate devices
                if dev['max_input_channels'] > 0: #Check if input
                    input_devices.append(i) #Add index to list
                    hostapi = sd.query_hostapis(dev['hostapi'])['name'] #Get host api name
                    print(f"{len(input_devices)}. {dev['name']} ({hostapi})") #Print device

            selection = int(input("\nSelect device number: ")) #Ask for selection
            
            if selection == 0: #If default device
                device_index = None
                dev_info = sd.query_devices(kind='input')
            elif selection > 0 and selection <= len(input_devices): #Validate selection
                device_index = input_devices[selection - 1] #Get real index
                dev_info = sd.query_devices(device_index)
            else:
                print("Invalid selection.")
                return None

            # Check device capabilities to avoid channel errors
            rec_channels = int(min(channel, dev_info['max_input_channels']))
            
            print(f"Starting record of {duration} seconds...") #Print start record message
            print(f"Recording from: {dev_info['name']} ({rec_channels} ch)")
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=rec_channels, dtype='int16', device=device_index) #Rec desktop
            sd.wait()  #Wait to rec finish

            if np.all(recording == 0):
                print("Warning: Recording is silent.\n- If on Linux: Open 'pavucontrol', go to 'Recording' tab, and change the source of this application to 'Monitor of...'.\n- If on Windows: Ensure 'Stereo Mix' is enabled and selected.")

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
    
        #Finish except

    #Finish function RecDesk

#RecMic()