"""

This file controls the StepSeq for the Sampling proyect

Created by:

Calak de Astora gh: https://github.com/elcalak

Suggest:
Compile in environment: Use Environment.sh to install all dependencies 
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk

"""

import json #Call json module
import tkinter as tk #Call tkinter module
from tkinter import filedialog #Call filedialog module
import audio_controls as ac #Call the module from Control audio

class StepSeqControls:

    """

    This class provides the control logic for the Step Sequencer mode. 
    It handles user interaction for adjusting tempo, managing multiple sequences, 
    displaying patterns, and performing file operations such as saving, 
    loading, and exporting to audio files.

    """

    def tempo(self, cmd): #Function to change tempo

        """
        Updates the playback tempo based on a user command. 
        The command is expected to be in the format 'tempo <value>'.
        It validates that the tempo is a positive integer and returns it.

        """

        try: #Try block to change tempo

            _, new_tempo = cmd.split() #Split command to get new tempo
            new_tempo = int(new_tempo) #Convert new tempo to integer

            if new_tempo > 0: #If new tempo is positive

                tempo = new_tempo #Set the new tempo
                print(f"Tempo set to {tempo} BPM.") #Set tempo message
                return tempo #Return new tempo

            else: #Else

                print("Tempo must be positive.") #Invalid tempo message

        except Exception: #Except block for invalid tempo command

            print("Invalid command format. Use: tempo BPM") #Invalid command message

    #End of tempo function

    def show(self, sequences, current_seq): #Function to show current sequence

        """
        Iterates through the current sequence and prints the assigned sample 
        indices for each step (1-16) to provide a visual overview of the pattern.

        """

        for i, sample_idxs in enumerate(sequences[current_seq]): #Iterate over the sequence

            if sample_idxs: #If there are sample indexes

                print(f"Step {i+1}: {sample_idxs}") #Print step and sample numbers

            else: #Else

                print(f"Step {i+1}: None") #Print step and None

    #End of show function

    def seq(self, cmd, sequences, current_seq, num_steps): #Function to change or create sequence

        """
        Allows the user to switch the active sequence or create a new one. 
        It processes the command string to identify the sequence name, 
        initializes it if it doesn't exist, and returns the updated 
        sequences dictionary and the new active sequence key.

        """

        try: #Try block to change or create sequence

            _, seq_name = cmd.split() #Get sequence name
            seq_name = seq_name.upper() #Convert to uppercase

            if seq_name not in sequences: #If sequence not exists

                sequences[seq_name] = [[] for _ in range(num_steps)] #Create new sequence
                print(f"Seq '{seq_name}' Created y selected.") #Created message

            else: #Else

                print(f"Seq '{seq_name}' Selected.") #Selected message

            current_seq = seq_name #Set current sequence
            return sequences, current_seq #Return sequences and current sequence

        except Exception: #Catch exception

            print("Format: seq Name") #Invalid format message

    #End of seq function

    def save_patterns(self, tempo, sequences, last_chain): #Function to save patterns

        """
        Saves the current state of the step sequencer, including tempo, 
        all sequence patterns, and the last played chain, to a JSON file. 
        Uses a Tkinter file dialog to allow the user to choose the save location.

        """

        try: #Try block to save patterns

            root = tk.Tk() #Create a Tk object
            root.withdraw() #Hide main dialog

            filename = filedialog.asksaveasfilename( #Open file dialog to chose name to save

                title="Save Patterns", #Title from Tk form
                defaultextension=".json", #Extension from archive
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")] #File type search

            )

            root.destroy() #Clean up Tk instance

            if filename: #Verify filename

                data = { #Data to save

                "tempo": tempo, #Tempo
                "sequences": sequences, #Sequences
                "last_chain": last_chain #Last played chain

                }

                with open(filename, 'w') as f: #Open file

                    json.dump(data, f, indent=4) #Dump json

                    print(f"Patterns saved successfully to {filename}") #Success message

            else: #Else

                print("Save cancelled.") #Cancelled message

        except Exception as e: #Catch errors

            print(f"Error saving patterns: {e}") #Error message

    #End of Save function

    def load_patterns(self): #Function to load patterns

        """
        Loads a previously saved sequencer state from a JSON file. 
        It updates the tempo, sequences dictionary, and last played chain 
        based on the loaded data and returns them.

        """

        # Initialize default values

        num_steps = 16 #Number of steps in the sequencer
        sequences = {}  # Index to multiple seq, ej: {'A': [...], 'B': [...]}
        current_seq = 'A' #Sequence currently being edited
        sequences[current_seq] = [[] for _ in range(num_steps)] #Start with A empty sequence
        tempo = 120  # Default tempo in BPM
        last_chain = [] # Variable to store the last played chain

        try: #Try block to load patterns

            root = tk.Tk() #Create a Tk object
            root.withdraw() #Hide main dialog

            filename = filedialog.askopenfilename( #Open file dialog to chose file
                title="Load Patterns", #Title from Tk form
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")] #File type search
            )

            root.destroy() #Clean up Tk instance

            if filename: #Verify filename

                with open(filename, 'r') as f: #Open file

                    data = json.load(f) #Load json

                if "tempo" in data: #Check tempo

                    tempo = data["tempo"] #Load tempo

                if "sequences" in data: #Check sequences

                    sequences = data["sequences"] #Load sequences

                if current_seq not in sequences: #Check if current seq exists

                    current_seq = list(sequences.keys())[0] #Set to first available

                if "last_chain" in data: #Check last chain

                    last_chain = data["last_chain"] #Load last chain
                    print(f"Loaded last chain: {last_chain}")

                print(f"Patterns loaded successfully from {filename}") #Success message
                return tempo, sequences, last_chain #Return loaded data

            else: #Else

                print("Load cancelled.") #Cancelled message

        except Exception as e: #Catch errors

            print(f"Error loading patterns: {e}") #Error message

    #End of Load function

    #Function to export WAV file
    def export(self, cmd, sequences, current_seq, tempo, sound, last_chain):

        """
        Exports sequence patterns to a WAV file. It determines which sequences 
        to export based on user command arguments, prompts for a filename 
        via a file dialog, and invokes the audio_controls module for rendering.

        """

        try: #Try block to export WAV file

            root = tk.Tk() #Create Tk
            root.withdraw() #Hide

            filename = filedialog.asksaveasfilename( #Ask filename

                title="Export WAV", #Title
                defaultextension=".wav", #Extension
                filetypes=[("WAV files", "*.wav")] #File types
            )

            root.destroy() #Destroy Tk

            if filename: #If filename is valid

                parts = cmd.split() #Split command
                seqs_to_export = [] #List to store sequences to export

                if len(parts) == 1: #If no args

                    if last_chain: seqs_to_export = last_chain #Use last chain
                    else: seqs_to_export = [current_seq] #Use current

                else: #Else, specific sequences provided

                    for s in parts[1:]: #Iterate over provided sequences

                        #Add to export list
                        if s.upper() in sequences: seqs_to_export.append(s.upper())
                        else: print(f"Sequence '{s}' not found.") #Not found message

                if seqs_to_export: #If there are sequences to export

                    #Call export from AudioControls
                    ac.export_wav(filename, seqs_to_export, sequences, tempo, sound)

                else: #Else, no sequences to export

                    print("Nothing to export.") #Nothing to export message

            else: #Else, invalid filename

                print("Export cancelled.") #Cancelled message

        except Exception as e: #Catch errors

            print(f"Error exporting: {e}") #Error message

    #End of export function

#End of StepSeqControls class
