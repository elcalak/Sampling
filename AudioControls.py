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
Compile in environment: Use Environment.sh to install all dependencies

"""

import pygame as pg #Call the module pygame as pg to playing audio
import numpy as np #Call numpy for audio array manipulation
from scipy.io import wavfile #Call wavfile to write wav files
import os #Call os for path checking

def load(file): #Function load files
    
    global sound, file_type
    sound = [None] * 10 #Global variable sound to save the current audio
    file_type = [None] * 10 #Global variable to known type of file
    
    print("Im load fun!") #Line for work check

    try: #Init try
        
        print("Hi im load try!") #Line for work check

        pg.mixer.init() #Start module mixer from pygame
        print("Hey im starting the mixer!") #Line for work check
        
        for i in range(1,10):

            if file[i].endswith(".mp3") or file[i].endswith(".ogg"): #Start condicional for compress format
            
                sound[i] = pg.mixer.music.load(file[i]) #Load MP3
                print(f"Im loadmp3 {i}!") #Line for work check
                file_type[i] = "mp3"
                #return pg.mixer.music, True #Return pygame mixer
            #Finish condicional for compress formats

            elif file[i].endswith(".wav"): #Start condicional for wav format
            
                sound[i] = pg.mixer.Sound(file[i]) #Load WAV
                print(f"Im loadwav {i}!") #Line for work check
                file_type[i] = "wav"
                #return sound, True #Return pygame mixer
            #Finish condicional for wav format

            else: #Start the last condicional 

               print("No supported format") #Print error menssage for no supported formats
            #Finish condicional
       
        #Finish for to load audio files

        print("Load fun Work Succes!") #Line for work check
        #print(sound) #Line for work check
        return sound, True #Return pygame mixer

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

def play(sample): #Function play

    global song_status
    song_status = [None] * 10 #Global variable playsound to save the current status of sound

    #print("Im play fun!") #Line for work check

    try: #Init try
        
        #print("Hi im play try!") #Line for work check

        if file_type == "mp3": #Start condicional for compress format
            
            pg.mixer.music.play() #Start play
            #print("Im playmp3 fun!") #Line for work check
            song_status = True
            return pg.mixer.music, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format
            
            global status_sound #Global variable playsound to save the current status of sound
            status_sound = sample.play() #Start play
            #print("Im playwav fun!") #Line for work check
            song_status = False
            return sound, True #Return pygame mixer
        #Finish condicional for wav format
       
    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none and false
    #Finish Except

#End Function play

def export_wav(filename, chain, sequences, tempo, sound_paths): #Function to export chain to wav
    
    print(f"Exporting to {filename}...") #Status message
    
    try: #Try block
        
        fs = 44100 #Sample rate
        beat_duration = 60 / tempo #Duration of a beat
        step_duration = beat_duration / 4 #Duration of a step (16th note)
        samples_per_step = int(step_duration * fs) #Samples per step
        
        loaded_samples = {} #Cache for loaded samples
        max_sample_len = 0 #Track max length for buffer calculation
        
        # Load samples into memory
        for i, path in sound_paths.items(): #Loop for all samples paths
        
            if path and os.path.exists(path): #Check if path exist
        
                try: #Try block to read wav file
        
                    s_fs, s_data = wavfile.read(path) #Read wav file
                    
                    # Normalize to float -1..1
                    if s_data.dtype == np.int16: #16-bit PCM
                        
                        s_data = s_data.astype(np.float32) / 32768.0 #Convert to float
                    
                    elif s_data.dtype == np.uint8: #8-bit PCM
                    
                        s_data = (s_data.astype(np.float32) - 128) / 128.0 #Convert to float
                    
                    # Ensure stereo
                    if len(s_data.shape) == 1: #Mono to stereo
                        
                        s_data = np.column_stack((s_data, s_data)) #Duplicate channel
                        
                    loaded_samples[i] = s_data #Store loaded sample
                    
                    if len(s_data) > max_sample_len: #Update max length
                    
                        max_sample_len = len(s_data) #Update max sample length
                        
                except Exception as e: #Catch read errors
        
                    print(f"Error reading {path}: {e}") #Error message
        
        # Calculate total length
        total_steps = len(chain) * 16 #Assuming 16 steps per sequence
        total_len = (total_steps * samples_per_step) + max_sample_len #Total length of output buffer
        
        output = np.zeros((total_len, 2), dtype=np.float32) #Create output buffer
        
        current_step = 0 #Step counter
        
        # Construct the sequence
        for seq_name in chain: #Loop for all sequences in chain
            
            if seq_name in sequences: #Check if sequence exist
            
                pattern = sequences[seq_name] #Get pattern
            
                for step_samples in pattern: #Loop for all steps in pattern
            
                    start_pos = current_step * samples_per_step #Calculate start position
            
                    if step_samples: #If there are samples assigned to this step
            
                        for slot_idx in step_samples: #Loop for all samples in step
            
                            if slot_idx in loaded_samples: #Check if sample is loaded
            
                                sample = loaded_samples[slot_idx] #Get sample
                                end_pos = start_pos + len(sample) #Calculate end position
            
                                if end_pos <= total_len: #Check bounds
            
                                    output[start_pos:end_pos] += sample #Mix sample
            
                    current_step += 1 #Increment step counter
        
        # Normalize output to prevent clipping
        max_val = np.max(np.abs(output)) #Find max value
        
        if max_val > 1.0: #If clipping
        
            output /= max_val #Normalize output
            
        wavfile.write(filename, fs, (output * 32767).astype(np.int16)) #Write file
        print(f"Export successful: {filename}") #Success message
        
    except Exception as e: #Catch all errors
        
        print(f"Export failed: {e}") #Error message

#End Function export_wav

def export_session_wav(filename, events, sound_paths): #Function to export session to wav
    
    print(f"Exporting session to {filename}...") #Status message

    try: #Try block
        
        fs = 44100 #Sample rate
        
        loaded_samples = {} #Cache for loaded samples
        max_sample_len = 0 #Track max length
        
        # Load samples into memory
        for i, path in sound_paths.items(): #Loop for all samples paths
            
            if path and os.path.exists(path): #Check if path exist
            
                try: #Try block to read wav file
            
                    s_fs, s_data = wavfile.read(path) #Read wav file
                    # Normalize to float -1..1
            
                    if s_data.dtype == np.int16: #16-bit PCM
            
                        s_data = s_data.astype(np.float32) / 32768.0 
            
                    elif s_data.dtype == np.uint8: #8-bit PCM
            
                        s_data = (s_data.astype(np.float32) - 128) / 128.0 
                    # Ensure stereo
            
                    if len(s_data.shape) == 1: #Mono to stereo
            
                        s_data = np.column_stack((s_data, s_data)) 
            
                    loaded_samples[i] = s_data #Store loaded sample
            
                    if len(s_data) > max_sample_len: #Update max length
            
                        max_sample_len = len(s_data) 
            
                except Exception as e: #Catch read errors
            
                    print(f"Error reading {path}: {e}") 
        
        if not events: #If no events
            
             print("No events to export.") 
             return

        # Calculate total length
        last_event_time = events[-1][0] 
        total_len = int(last_event_time * fs) + max_sample_len + 44100 # Add 1 sec buffer
        output = np.zeros((total_len, 2), dtype=np.float32) #Create output buffer
        
        for offset, slot_idx in events:
            
            if slot_idx in loaded_samples:
            
                sample = loaded_samples[slot_idx]
                start_pos = int(offset * fs)
                end_pos = start_pos + len(sample)
            
                if end_pos <= total_len:
            
                    output[start_pos:end_pos] += sample
        
        # Normalize output
        max_val = np.max(np.abs(output)) 
        
        if max_val > 1.0: 
        
            output /= max_val 
            
        wavfile.write(filename, fs, (output * 32767).astype(np.int16)) #Write file
        
        print(f"Export successful: {filename}") 
        
    except Exception as e: #Catch all errors
        
        print(f"Export failed: {e}") 

#End Function export_session_wav

def pause(): #Function pause

    #print("Im pause fun!") #Line for work check

    try: #Init try
        
        #print("Hi im pause try!") #Line for work check

        if song_status == True or status_sound.get_busy() == True: #Start condicional know if music is played
        
            if file_type == "mp3": #Start condicional for compress format
            
                pg.mixer.music.pause() #Start pause
                #print("Im pausemp3 fun!") #Line for work check
                return pg.mixer.music, True #Return pygame mixer
            #Finish condicional for compress formats

            else: #Start condicional for wav format
            
                status_sound.pause() #Start pause
                #print("Im pausewav fun!") #Line for work check
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

    #print("Im resume fun!") #Line for work check

    try: #Init try
        
        print("Hi im resume try!") #Line for work check

        if song_status == True or status_sound.get_busy() == True: #Start condicional know if music is played
        
            if file_type == "mp3": #Start condicional for compress format
            
                pg.mixer.music.unpause() #Start resume
                #print("Im resumemp3 fun!") #Line for work check
                return pg.mixer.music, True #Return pygame mixer
            #Finish condicional for compress formats

            else: #Start condicional for wav format
            
                status_sound.unpause() #Start resume
                #print("Im resumewav fun!") #Line for work check
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

def stop(sample): #Function stop
    
    #print("Im stop fun!") #Line for work check

    try: #Init try
        
        #print("Hi im a stop try!") #Line for work check

        if file_type == "mp3": #Start condicional for compress format
            
            pg.mixer.music.stop() #Stop play
            #print("Im stopmp3 fun!") #Line for work check
            return pg.mixer.music, True #Return pygame mixer
        #Finish condicional for compress formats

        else: #Start condicional for wav format

            sample.stop() #Stop play
            #print("Im stopwav fun!") #Line for work check
            return sound, True #Return pygame mixer
        #Finish condicional for wav format

    #Finish Try 
    
    except pg.error as e: #Init except
    
        print(f"Error to load or play the file: {sample}") #Print error message
        print(f"Pygame error: {e}") #Print error message
        return None, False #Return none add false
    #Finish Except

#End Function stop

"""#Function checks:

print("Im alavie")
archivo = '/home/elcalak/Repositories/elcalak/Sampling/Records/recording_20250511_222232.wav'
load(archivo)
play()
sleep(5)
pause()
sleep(5)
resume()
sleep(5)
stop()

#"""