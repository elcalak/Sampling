"""

This file controls the audio recording for the Sampling proyect

Created by:

Calak de Astora gh: https://github.com/elcalak

Suggest:
Compile in environment: Use Environment.sh to install all dependencies

"""

import os #Call the module os to control path files
import datetime #Call the module datetime to control date
import sounddevice as sd #Call the module sounddevice as sd for record audio
import numpy as np #Call numpy for control of audio arrays
from scipy.io.wavfile import write #Call function write from the module scipy

class RecordSamp: #Start class RecordSamp

    """
    This class contains functions to record audio from the microphone or the desktop.
    It uses the sounddevice library to record audio
    and the scipy library to save the audio to a WAV file.
    The class provides a simple interface for users
    to record audio from the microphone or the desktop,
    with options to select the duration and the audio device.
    The recorded audio is saved to a WAV file in the "Records" or "Record desktop" directory.
    
    """

    def rec_mic(self, duration, fs=44100): #Function Record microphone

        """
        This function records audio from the microphone for a specified duration.
        It uses the sounddevice library to capture the audio
        and saves it as a WAV file using the scipy library.
         - duration: The recording duration in seconds.
         - fs: The sampling rate (default: 44100 Hz).
        The recorded audio is saved to a WAV file in the "Records" directory with a unique filename
        based on the current timestamp.
        """
        print(f"Starting record of {duration} seconds...") #Print start record message

        try: #Init try

            recording = sd.rec(
            int(duration * fs), samplerate=fs, channels=2, dtype='int16'
            ) #Rec microphone on stereo
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

    def rec_desk(self, duration, fs=44100, channel = 2): #Function Record Desktop

        """
        This function records audio from the desktop for a specified duration.
        It uses the sounddevice library to capture the audio
        and saves it as a WAV file using the scipy library.
         - duration: The recording duration in seconds.
         - fs: The sampling rate (default: 44100 Hz).
         - channel: Number of channels to record (default: 2).
        The recorded audio is saved to a WAV file in
        the "Record desktop" directory with a unique filename
        based on the current timestamp.

        This functions dont works, its in working progress

        """

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
            recording = sd.rec(
            int(duration * fs), samplerate=fs,
            channels=rec_channels, dtype='int16', device=device_index
            ) #Rec desktop
            sd.wait()  #Wait to rec finish

            if np.all(recording == 0):
                print("Warning: Recording is silent." \
                "\n- If on Linux: Open 'pavucontrol', go to 'Recording' tab, "
                "and change the source of this application to 'Monitor of...'." \
                "\n- If on Windows: Ensure 'Stereo Mix' is enabled and selected.")

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
