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
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk
"""

from time import sleep #From module time import sleep function
import os #Call os module
import numpy as np #Call numpy
from scipy.io import wavfile #Call wavfile
from scipy import signal #Call signal from scipy
import AudioControls as ac #Call the module AudioControls as ac to control the audio
import tkinter as tk #Call tkinter
from tkinter import filedialog #Call filedialog

class EditSamp:

    def EzChop(self, num_slices): #Function to chop sample into slices with a simple interface
        
        root = tk.Tk() #Create a Tkinter root window
        root.withdraw() #Hide the root window
        sample_path = filedialog.askopenfilename(title="Select Sample to Chop", filetypes=[("WAV files", "*.wav")]) #Open file dialog to select sample to chop
        root.destroy() #Destroy the root window after file selection
        
        if not sample_path: #If no file is selected
            print("No file selected.") #Print no file selected message
            return [] #Return empty list
            
        print(f"Chopping {sample_path} into {num_slices} slices...") #Print chopping message with file path and number of slices

        try: #Init try
            
            fs, data = wavfile.read(sample_path) #Read wav file
            
            total_samples = len(data) #Get total number of samples in the audio file
            samples_per_slice = total_samples // num_slices #Calculate number of samples per slice
            
            base_name = os.path.splitext(os.path.basename(sample_path))[0] #Get base name of the file without extension
            output_dir = os.path.join(os.path.dirname(sample_path), base_name) #Define output directory as a subfolder with the same name as the file
            
            if not os.path.exists(output_dir): #If output directory does not exist
                os.makedirs(output_dir) #Create output directory
                
            chopped_paths = [] #List to store paths of chopped slices
            
            for i in range(num_slices): #Loop through the number of slices
                start = i * samples_per_slice #Calculate start index for the current slice
                end = start + samples_per_slice if i < num_slices - 1 else total_samples #Calculate end index for the current slice, ensuring the last slice includes any remaining samples
                
                slice_data = data[start:end] #Extract the slice data from the original audio data
                
                slice_filename = f"{base_name}_chop_{i+1}.wav" #Create filename for the slice
                slice_path = os.path.join(output_dir, slice_filename) #Define path for the slice
                
                wavfile.write(slice_path, fs, slice_data) #Save the slice as a new wav file
                chopped_paths.append(slice_path) #Add the slice path to the list of chopped paths
                print(f"Saved slice {i+1}: {slice_path}") #Print message confirming the slice has been saved with its path
            
            sleep(2) #Sleep 2 seconds to allow the user to read the messages about the saved slices

            return chopped_paths #Return the list of chopped paths

        except Exception as e: #Init except
           
            print(f"Error chopping sample: {e}") #Print error message if there is an issue during the chopping process
            sleep(2) #Sleep 2 seconds to allow the user to read the error message

            return [] #Return empty list if there was an error

    #End of EzChop function        
    
    def Catch(self, launch):

        root = tk.Tk() #Create a Tkinter root window
        root.withdraw() #Hide the root window
        sample_path = filedialog.askopenfilename(title="Select Sample:", filetypes=[("WAV files", "*.wav")]) #Open file dialog to select sample to filter
        root.destroy() #Destroy the root window after file selection

        if not sample_path: #If no file is selected
            
            print("No file selected.") #Print no file selected message
            sleep(1) #Sleep 1 second
            
            return None #Return None if no file is selected

        if launch: #If launch is true, it means the function was called from the main menu

            self.FilterPass(sample_path) #Call the FilterPass function to apply a filter to the selected sample
        
        else: #Else if launch is False, it means the function was called from the filter menu
        
            self.PitchControl(sample_path) #Call the PitchControl function to apply pitch control to the selected sample

    def FilterPass(self,sample_path): #Function to apply a filter to a sample
                
        type = input("Enter filter type (lowpass/highpass) with lp and hp: ").strip().lower() #Input filter type and convert to lowercase

        if type == "lp": #If input is lp
        
            filter_type = "lowpass" #Set filter type to lowpass
        
        elif type == "hp": #Else if input is hp
        
            filter_type = "highpass" #Set filter type to highpass
        
        else: #Else if input is not recognized
           
            print("Invalid filter type. Please choose 'lp' for lowpass or 'hp' for highpass.") #Print invalid filter type message
            sleep(1) #Sleep 1 second
            return None #Return None if the filter type is invalid

        cutoff_freq = float(input("Enter cutoff frequency in Hz: ").strip()) #Input cutoff frequency and convert to float

        print(f"\tApplying {filter_type} filter with cutoff frequency {cutoff_freq} Hz to {sample_path}...") #Print message about the filter being applied
        sleep(1) #Sleep 1 second

        try: #Init try
            
            fs, data = wavfile.read(sample_path) #Read wav file
            
            if filter_type == "lowpass": #If filter type is lowpass
                
                print("Hi im lowpass filter") #Print message about implementing lowpass filter
                sleep(1) #Sleep 1 second

                nyq = 0.5 * fs
                normal_cutoff = cutoff_freq / nyq
                b, a = signal.butter(5, normal_cutoff, btype='low', analog=False)
                filtered_data = signal.filtfilt(b, a, data, axis=0)
            
            elif filter_type == "highpass": #Else if filter type is highpass
            
                nyq = 0.5 * fs
                normal_cutoff = cutoff_freq / nyq
                b, a = signal.butter(5, normal_cutoff, btype='high', analog=False)
                filtered_data = signal.filtfilt(b, a, data, axis=0)
            
            base_name = os.path.splitext(os.path.basename(sample_path))[0] #Get base name of the file without extension
            output_filename = f"{base_name}_{filter_type}_cutoff_{int(cutoff_freq)}Hz.wav" #Create filename for the filtered sample
            output_path = os.path.join(os.path.dirname(sample_path), output_filename) #Define path for the filtered sample
            
            wavfile.write(output_path, fs, filtered_data.astype(np.int16)) #Save the filtered data as a new wav file
            
            sample = [" "] * 10 #Create a list with the path of the filtered sample to load it with AudioControls
            sample[1] = output_path #Set the first element of the list to the path of the filtered sample

            PlaySample_Tuple = ac.load(sample) #Load the filtered audio using the load function from AudioControls
            PlaySample_List = PlaySample_Tuple[0] #Get the first element of the tuple returned by the load function, which is the filtered audio data
            PlaySample = PlaySample_List[1] #Get the first element of the list, which is the filtered audio data to be played

            print("Filter applied successfully. Playing filtered audio...") #Print message confirming the filter was applied and the audio is playing
            ac.play(PlaySample) #Play the filtered audio using the play function from AudioControls

            option = input("Do you want to save the filtered sample? (y/n): ").strip().lower() #Input option to save the filtered sample and convert to lowercase

            if option == 'y': #If the user does want to save the filtered sample            
                
                ac.stop(PlaySample) 

                print(f"Filtered sample saved: {output_path}") #Print message confirming the filtered sample has been saved with its path
                
                return output_path #Return the path of the filtered sample

            elif option == 'n': #Else if the user does not want to save the filtered sample
                
                ac.stop(PlaySample) #Stop the audio playback using the stop function from AudioControls

                try:
                    
                    os.remove(output_path)
                
                except OSError as e:
                
                    print(f"Error deleting temporary file: {e}")

                print("Filtered sample not saved.") #Print message confirming the filtered sample was not saved
                
                new_option = input("Do you want try with other parammters? (y/n): ").strip().lower() #Input option to apply another filter and convert to lowercase

                if new_option == 'y': #If the user does want to apply another filter
                    
                    self.FilterPass(sample_path) #Call the FilterPass function again to apply another filter

                elif new_option == 'n': #Else if the user does not want to apply another filter
                    
                    print("Exiting filter mode.") #Print message confirming exit from filter mode
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function
                
                else: #Else if the input is not recognized
                    
                    print("Invalid option. Exiting filter mode.") #Print invalid option message
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

            else: #Else if the input is not recognized
                
                ac.stop(PlaySample) #Stop the audio playback using the stop function from AudioControls
                
                print("Invalid option. Exiting filter mode without changes.") #Print invalid option message
                
                try:
                    
                    os.remove(output_path)
                
                except OSError as e:
                
                    print(f"Error deleting temporary file: {e}")
                
                sleep(1) #Sleep 1 second

                return None #Return None to exit the function


        except Exception as e: #Init except
            
            print(f"Error applying filter: {e}") #Print error message if there is an issue during the filtering process
            sleep(1) #Sleep 1 second

            return None #Return None if there was an error

    #End of FilterPass function

    def PitchControl(self, sample_path): #Function to apply pitch control to a sample
        
        semitones = float(input("Enter number of semitones to shift (positive(+) for up, negative(-) for down): ").strip()) #Input number of semitones to shift and convert to float

        print(f"\tApplying pitch shift of {semitones} semitones to {sample_path}...") #Print message about the pitch shift being applied
        sleep(1) #Sleep 1 second

        try: #Init try
            
            fs, data = wavfile.read(sample_path) #Read wav file
            
            factor = 2 ** (semitones / 12) #Calculate the pitch shift factor based on the number of semitones
            
            indices = np.round(np.arange(0, len(data), factor)).astype(int) #Calculate new indices for the audio data based on the pitch shift factor
            indices = indices[indices < len(data)] #Ensure that the new indices do not exceed the length of the original audio data
            
            pitched_data = data[indices] #Create the new audio data by selecting samples at the new indices
            
            base_name = os.path.splitext(os.path.basename(sample_path))[0] #Get base name of the file without extension
            output_filename = f"{base_name}_pitch_shift_{int(semitones)}_semitones.wav" #Create filename for the pitch-shifted sample
            output_path = os.path.join(os.path.dirname(sample_path), output_filename) #Define path for the pitch-shifted sample
            
            wavfile.write(output_path, fs, pitched_data.astype(np.int16)) #Save the pitch-shifted data as a new wav file
            
            sample = [" "] * 10 #Create a list with the path of the filtered sample to load it with AudioControls
            sample[1] = output_path #Set the first element of the list to the path of the filtered sample

            PlaySample_Tuple = ac.load(sample) #Load the filtered audio using the load function from AudioControls
            PlaySample_List = PlaySample_Tuple[0] #Became the tuple to a list
            PlaySample = PlaySample_List[1] #Get the first element of the list, which is the pitchet audio data to be played

            print("Filter applied successfully. Playing Pitched audio...") #Print message confirming the pitch was applied and the audio is playing
            ac.play(PlaySample) #Play the filtered audio using the play function from AudioControls

            option = input("Do you want to save the filtered sample? (y/n): ").strip().lower() #Input option to save the filtered sample and convert to lowercase

            if option == 'y': #If the user does want to save the filtered sample            
                
                ac.stop(PlaySample) #Stop the audio playback using the stop function from AudioControls

                print(f"Pitched sample saved: {output_path}") #Print message confirming the filtered sample has been saved with its path
            
                return output_path #Return the path of the filtered sample

            elif option == 'n': #Else if the user does not want to save the filtered sample
                
                ac.stop(PlaySample) #Stop the audio playback using the stop function from AudioControls

                try:
                    
                    os.remove(output_path)
                
                except OSError as e:
                
                    print(f"Error deleting temporary file: {e}")

                print("Filtered sample not saved.") #Print message confirming the filtered sample was not saved
                
                new_option = input("Do you want try with other parammters? (y/n): ").strip().lower() #Input option to apply another filter and convert to lowercase

                if new_option == 'y': #If the user does want to apply another filter
                    
                    self.PitchControl(sample_path) #Call the PitchControl function again to apply another filter

                elif new_option == 'n': #Else if the user does not want to apply another filter
                    
                    print("Exiting filter mode.") #Print message confirming exit from filter mode
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function
                
                else: #Else if the input is not recognized
                    
                    print("Invalid option. Exiting filter mode.") #Print invalid option message
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

            else:
                
                ac.stop(PlaySample) #Stop the audio playback using the stop function from AudioControls
                
                print("Invalid option. Exiting filter mode without changes.") #Print invalid option message
                
                try:
                    
                    os.remove(output_path)
                
                except OSError as e:
                
                    print(f"Error deleting temporary file: {e}")
                
                sleep(1) #Sleep 1 second

                return None #Return None to exit the functio

        except Exception as e: #Init except
            
            print(f"Error applying pitch shift: {e}") #Print error message if there is an issue during the pitch shifting process
            sleep(1) #Sleep 1 second

            return None #Return None if there was an error

#End of EditSamp class