"""

This file controls the audio for the Sampling proyect

Created by:

Calak de Astora gh: https://github.com/elcalak

Suggest:
Compile in environment: Use Environment.sh to install all dependencies
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk
"""

from time import sleep #From module time import sleep function
import os #Call os module
import tkinter as tk #Call tkinter
from tkinter import filedialog as fl #Call filedialog
import numpy as np #Call numpy
from scipy.io import wavfile #Call wavfile
from scipy import signal #Call signal from scipy
import audio_controls as ac #Call the module AudioControls as ac to control the audio

class EditSamp:

    """
    Class EditSamp contains functions to edit audio samples, including chopping samples into slices, 
    applying filters, and controlling pitch.
    It provides a simple interface for users to select audio files and apply
    various audio processing techniques, with options
    to save the edited samples or try different parameters.
    The class uses the scipy library for audio processing
    and tkinter for file selection dialogs, making it a versatile tool for audio
    editing in the context of the Sampling project.

    """

    def ez_chop(self, num_slices): #Function to chop sample into slices with a simple interface #pylint: disable=too-many-locals

        """

        This function allows the user to select a WAV audio file
        and chop it into a specified number of slices.
        The user is prompted to select a file using
        a file dialog, and then the function reads the audio data,
        calculates the number of samples per slice,
        and saves each slice as a new WAV file in a subdirectory named after the original file.
        The function also handles errors that may occur during the chopping process and
        provides feedback to the user about the progress
        and results of the operation.
        The paths of the chopped slices are returned as a
        list for further use in the Sampling project,
        allowing for easy integration with other audio processing functions.

        """

        root = tk.Tk() #Create a Tkinter root window
        root.withdraw() #Hide the root window
        # Open file dialog to select sample to chop
        sample_path = fl.askopenfilename(
            title="Select Sample to Chop", filetypes=[("WAV files", "*.wav")]
        )
        root.destroy() #Destroy the root window after file selection

        if not sample_path: #If no file is selected

            print("No file selected.") #Print no file selected message

            return [] #Return empty list

        # Print chopping message with file path and number of slices
        print(f"Chopping {sample_path} into {num_slices} slices...")

        try: #Init try

            fs, data = wavfile.read(sample_path) #Read wav file

            total_samples = len(data) #Get total number of samples in the audio file
            samples_per_slice = total_samples // num_slices #Calculate number of samples per slice

            # Get base name of the file without extension
            base_name = os.path.splitext(os.path.basename(sample_path))[0]
            # Define output directory as a subfolder with the same name as the file
            output_dir = os.path.join(os.path.dirname(sample_path), base_name)

            if not os.path.exists(output_dir): #If output directory does not exist
                os.makedirs(output_dir) #Create output directory

            chopped_paths = [] #List to store paths of chopped slices

            for i in range(num_slices): #Loop through the number of slices
                start = i * samples_per_slice #Calculate start index for the current slice
                # Calculate end index for the current slice, ensuring the last slice includes
                # any remaining samples
                end = start + samples_per_slice if i < num_slices - 1 else total_samples

                slice_data = data[start:end] #Extract the slice data from the original audio data

                slice_filename = f"{base_name}_chop_{i+1}.wav" #Create filename for the slice
                slice_path = os.path.join(output_dir, slice_filename) #Define path for the slice

                wavfile.write(slice_path, fs, slice_data)  # Save the slice as a new wav file
                chopped_paths.append(slice_path) #Add the slice path to the list of chopped paths
                # Print message confirming the slice has been saved with its path
                print(f"Saved slice {i+1}: {slice_path}")

            sleep(2) #Sleep 2 seconds to allow the user to read the messages about the saved slices

            return chopped_paths #Return the list of chopped paths

        except Exception as e: #Init except #pylint: disable=broad-exception-caught

            # Print error message if there is an issue during the chopping process
            print(f"Error chopping sample: {e}")
            sleep(2) #Sleep 2 seconds to allow the user to read the error message

            return [] #Return empty list if there was an error

    #End of EzChop function

    def catch(self, launch):

        """
        This function allows the user to
        select a WAV audio file and apply either a filter or pitch control to it,
        depending on the context in which the function is called.
        If the function is called from the main menu (launch is True),
        it will prompt the user to apply a filter to the selected sample.
        If the function is called from the filter menu (launch is False),
        it will prompt the user to apply pitch control to the selected sample.
        The function uses a file dialog for the user to select the audio file,
        and then calls the appropriate processing function based on the context.
        It also handles cases where no file is selected
        and provides feedback to the user about the actions being taken,
        making it a versatile tool for audio editing in the Sampling project. 
        The function serves as a central point for initiating different audio processing techniques
        based on user input and the context of the operation,
        streamlining the workflow for editing audio samples.

        """

        root = tk.Tk() #Create a Tkinter root window
        root.withdraw() #Hide the root window
        # Open file dialog to select sample to filter
        sample_path = fl.askopenfilename(
            title="Select Sample:", filetypes=[("WAV files", "*.wav")])
        root.destroy() #Destroy the root window after file selection

        if not sample_path: #If no file is selected

            print("No file selected.") #Print no file selected message
            sleep(1) #Sleep 1 second

            #return None #Return None if no file is selected

        if launch: #If launch is true, it means the function was called from the main menu

            # Call the FilterPass function to apply a filter to the selected sample
            self.filter_pass(sample_path)

        else: #Else if launch is False, it means the function was called from the filter menu

            # Call the PitchControl function to apply pitch control to the selected sample
            self.pitch_contol(sample_path)

    def filter_pass(self,sample_path): #Function to apply a filter to a sample #pylint: disable=too-many-locals

        """
        This function allows the user to apply either
        a lowpass or highpass filter to a selected WAV audio file.
        The user is prompted to input
        the filter type (lowpass or highpass) and the cutoff frequency in Hz.
        The function then applies the chosen filter
        to the audio data using the Butterworth filter design from the scipy library,
        saves the filtered audio as a new WAV file, and 
        providesoptions for the user
        to play the filtered audio and decide whether to save the filtered sample or not.
        If the user chooses not to save the filtered sample,
        the function offers the option
        to apply another filter with different parametersor exit the filter mode,
        making it a flexible tool for audio editing in the Sampling project. 
        The function also handles errors that may occur during
        the filtering process and provides feedback to the user about the actions being taken,
        ensuring a smooth user experience while editing audio samples.

        """

        # Input filter type and convert to lowercase
        type_prompt = "Enter filter type (lowpass/highpass) with lp and hp: "
        user_type = input(type_prompt).strip().lower()

        if user_type == "lp": #If input is lp

            filter_type = "lowpass"  # Set filter type to lowpass

        elif user_type == "hp": #Else if input is hp

            filter_type = "highpass"  # Set filter type to highpass

        else: #Else if input is not recognized

            # Print invalid filter type message
            print("Invalid filter type. Please choose 'lp' for lowpass or 'hp' for highpass.")
            sleep(1) #Sleep 1 second
            return None #Return None if the filter type is invalid

        #Input cutoff frequency and convert to float
        cutoff_freq = float(input("Enter cutoff frequency in Hz: ").strip())

        #Print message about the filter being applied
        print(f"\tApplying {filter_type} filter with cutoff frequency {cutoff_freq} Hz to {sample_path}...")  # pylint: disable=line-too-long
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

            # Get base name of the file without extension
            base_name = os.path.splitext(os.path.basename(sample_path))[0]
            # Create filename for the filtered sample
            output_filename = f"{base_name}_{filter_type}_cutoff_{int(cutoff_freq)}Hz.wav"
            # Define path for the filtered sample
            output_path = os.path.join(os.path.dirname(sample_path), output_filename)

            # Save the filtered data as a new wav file
            wavfile.write(output_path, fs, filtered_data.astype(np.int16))

            # Create a list with the path of the filtered sample to load it with AudioControls
            sample = [" "] * 10
            # Set the first element of the list to the path of the filtered sample
            sample[1] = output_path

            # Load the filtered audio using the load function from AudioControls
            play_sample_tuple = ac.load(sample)
            # Get the first element of the tuple returned by the load function,
            # which is the filtered audio data
            play_sample_list = play_sample_tuple[0]
            # Get the first element of the list, which is the filtered audio data to be played
            play_sample = play_sample_list[1]

            # Print message confirming the filter was applied and the audio is playing
            print("Filter applied successfully. Playing filtered audio...")
            ac.play(play_sample) #Play the filtered audio using the play function from AudioControls

            # Input option to save the filtered sample and convert to lowercase
            option = input("Do you want to save the filtered sample? (y/n): ").strip().lower()

            if option == 'y': #If the user does want to save the filtered sample

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                # Print message confirming the filtered sample has been saved with its path
                print(f"Filtered sample saved: {output_path}")

                return output_path #Return the path of the filtered sample

            elif option == 'n': #Else if the user does not want to save the filtered sample

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                try:

                    #Delete the temporary filtered file if the user does not want to save it
                    os.remove(output_path)

                except OSError as e: #Catch any OSError that occurs during file deletion and print an error message #pylint: disable=broad-exception-caught

                    print(f"Error deleting temporary file: {e}")

                # Print message confirming the filtered sample was not saved
                print("Filtered sample not saved.")

                # Input option to apply another filter and convert to lowercase
                new_option_prompt = "Do you want try with other parammters? (y/n): "
                new_option = input(new_option_prompt).strip().lower()

                if new_option == 'y': #If the user does want to apply another filter

                    # Call the FilterPass function again to apply another filter
                    self.filter_pass(sample_path)

                elif new_option == 'n': #Else if the user does not want to apply another filter

                    print("Exiting filter mode.") #Print message confirming exit from filter mode
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

                else: #Else if the input is not recognized

                    print("Invalid option. Exiting filter mode.") #Print invalid option message
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

            else: #Else if the input is not recognized

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                # Print invalid option message
                print("Invalid option. Exiting filter mode without changes.")

                try:

                    os.remove(output_path)

                except OSError as e:

                    print(f"Error deleting temporary file: {e}")

                sleep(1) #Sleep 1 second

                return None #Return None to exit the function

        except Exception as e: #Init except #pylint: disable=broad-exception-caught

            # Print error message if there is an issue during the filtering process
            print(f"Error applying filter: {e}")
            sleep(1) #Sleep 1 second

            return None #Return None if there was an error

    #End of FilterPass function

    def pitch_contol(self, sample_path): #Function to apply pitch control to a sample #pylint: disable=too-many-locals

        """

        This function allows the user to apply pitch control to a selected WAV audio file.
        The user is prompted to input the number of semitones to shift the audio data,
        with positive values for pitch shifting up and negative values for pitch shifting down.
        The function then applies the pitch shift to the audio data
        by resampling it according to the calculated pitch shift factor,
        saves the pitch-shifted audio as a new WAV file, and provides options for the
        user to play the pitch-shifted audio and decide whether
        to save the pitch-shifted sample or not.
        If the user chooses not to save the pitch-shifted sample, the function offers the
        option to apply another pitch shift with
        different parameters or exit the pitch control mode,
        making it a flexible tool for audio editing in the Sampling project.
        The function also handles errors that may occur during
        the pitch shifting process and provides feedback to the
        user about the actions being taken,
        ensuring a smooth user experience while editing audio samples.

        """

        # Input number of semitones to shift and convert to float
        semitones_prompt = (
            "Enter number of semitones to shift (positive(+) for up, negative(-) for down): "
        )
        semitones = float(input(semitones_prompt).strip())

        print(f"\tApplying pitch shift of {semitones} semitones to {sample_path}...")
        sleep(1) #Sleep 1 second

        try: #Init try

            fs, data = wavfile.read(sample_path) #Read wav file

            # Calculate the pitch shift factor based on the number of semitones
            factor = 2 ** (semitones / 12)

            # Calculate new indices for the audio data based on the pitch shift factor
            indices = np.round(np.arange(0, len(data), factor)).astype(int)
            # Ensure that the new indices do not exceed the length of the original audio data
            indices = indices[indices < len(data)]

            # Create the new audio data by selecting samples at the new indices
            pitched_data = data[indices]

            # Get base name of the file without extension
            base_name = os.path.splitext(os.path.basename(sample_path))[0]
            # Create filename for the pitch-shifted sample
            output_filename = f"{base_name}_pitch_shift_{int(semitones)}_semitones.wav"
            # Define path for the pitch-shifted sample
            output_path = os.path.join(os.path.dirname(sample_path), output_filename)

            # Save the pitch-shifted data as a new wav file
            wavfile.write(output_path, fs, pitched_data.astype(np.int16))

            # Create a list with the path of the filtered sample to load it with AudioControls
            sample = [" "] * 10
            # Set the first element of the list to the path of the filtered sample
            sample[1] = output_path

            # Load the filtered audio using the load function from AudioControls
            play_sample_tuple = ac.load(sample)
            play_sample_list = play_sample_tuple[0]  # Became the tuple to a list
            # Get the first element of the list, which is the pitchet audio data to be played
            play_sample = play_sample_list[1]

            # Print message confirming the pitch was applied and the audio is playing
            print("Filter applied successfully. Playing Pitched audio...")
            ac.play(play_sample) #Play the filtered audio using the play function from AudioControls

            # Input option to save the filtered sample and convert to lowercase
            option = input("Do you want to save the filtered sample? (y/n): ").strip().lower()

            if option == 'y': #If the user does want to save the filtered sample

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                # Print message confirming the filtered sample has been saved with its path
                print(f"Pitched sample saved: {output_path}")

                return output_path #Return the path of the filtered sample

            elif option == 'n': #Else if the user does not want to save the filtered sample

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                try:

                    #Delete the temporary pitch-shifted file if the user does not want to save it
                    os.remove(output_path)

                except OSError as e: #Catch any OSError that occurs during file deletion and print an error message #pylint: disable=broad-exception-caught

                    #Print error message if there was an issue deleting the temporary file
                    print(f"Error deleting temporary file: {e}")

                # Print message confirming the filtered sample was not saved
                print("Filtered sample not saved.")

                # Input option to apply another filter and convert to lowercase
                new_option_prompt = "Do you want try with other parammters? (y/n): "
                new_option = input(new_option_prompt).strip().lower()

                if new_option == 'y': #If the user does want to apply another filter

                    # Call the PitchControl function again to apply another filter
                    self.pitch_contol(sample_path)

                elif new_option == 'n': #Else if the user does not want to apply another filter

                    print("Exiting filter mode.") #Print message confirming exit from filter mode
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

                else: #Else if the input is not recognized

                    print("Invalid option. Exiting filter mode.") #Print invalid option message
                    sleep(1) #Sleep 1 second

                    return None #Return None to exit the function

            else:

                ac.stop(play_sample)  # Stop the audio playback using the stop function

                # Print invalid option message
                print("Invalid option. Exiting filter mode without changes.")

                try:

                    #Delete the temporary pitch-shifted file if the user does not want to save it
                    os.remove(output_path)

                except OSError as e: #Catch any OSError that occurs during file deletion and print an error message #pylint: disable=broad-exception-caught

                    print(f"Error deleting temporary file: {e}")

                sleep(1) #Sleep 1 second

                return None #Return None to exit the functio

        except Exception as e: #Init except #pylint: disable=broad-exception-caught

            # Print error message if there is an issue during the pitch shifting process
            print(f"Error applying pitch shift: {e}")
            sleep(1) #Sleep 1 second

            return None #Return None if there was an error

#End of EditSamp class
