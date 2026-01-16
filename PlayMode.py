"""

This file controls the Play modes for the Sampling proyect

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

import os #Import os library
from time import sleep #From module time import sleep function
import AudioBank as ab #Call the module from Control audio banks
import AudioControls as ac #Call the module from Control audio
import RecordSamp as rs #Call the module from Record Samples
import sys #Call sys module 
import termios #Call termios module
import tty #Call tty module
import json #Call json module
import tkinter as tk #Call tkinter module
from tkinter import filedialog #Call filedialog module

class PlayModes:

    def __init__(self): #Init contructor for PlayModes

        print("PlayModes initialized") #Work check
        
        sleep(1) #Sleep 1 second
        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
    
    #End contructor

    def FingerDrum(self, sound): #Start function fingerdrum with sound parameter

         #***This function will be change for Micros***" 
            
            key_sample_map = {} #Create a dictionary to map keys to samples

            slots_tuple = ac.load(sound) # Load samples using AudioControls module
            slots = slots_tuple[0] #Convert the sample tuple to a list

            KeyMapIndex = ['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n'] #Create a Index for keys

            for i in range(1, 10): # Map keys to sample names or indices

                key = KeyMapIndex[i - 1] #Get the corresponding key from the index

                if i < len(slots) and slots[i] is not None: #Verify to slot exist
                    
                    key_sample_map[key] = slots[i]  # Map key to the corresponding sample
                    print(f"Key '{key}' mapped to sample '{slots[i]}'") #Succes message

                else: #Else
                    
                    key_sample_map[key] = None  # No sample loaded for this slot  
                    print(f"Key '{key}' has no sample loaded.") #Info Message
            
            print("Mapping Succes!") #Work check line

            sleep(1) #Sleep 1 seconds

            os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen

            print("\tFinger Drumming Mode") #Title message
            print("Press keys (r ,t ,y ,f ,g ,h ,v ,n to play slot 1 to 9 respected) to play samples. Press 'q' to quit and 's' to save bank.") #Instructions message

            def getch(): #Function to get a single character from standard input without echoing to the screen
                
                fd = sys.stdin.fileno() #Get the file descriptor for standard input
                old_settings = termios.tcgetattr(fd) #Save the current terminal settings
                
                try: #Init try
                    
                    tty.setraw(fd) #Set the terminal to raw mode
                    ch = sys.stdin.read(1) #Read a single character
                
                finally: #Finally
                    
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #Restore the terminal settings
                
                return ch #Return the character read

            while True: #Infinite loop to capture key presses
                
                key = getch() #Get a single character input
                
                if key == 'q': #If key is 'q'
                    
                    print("Exiting Finger Drumming Mode.") #Exit message
                    break #Break the loop
                
                elif key == 's': #If key is 's'
                
                    ab.SaveBank()  # Call SaveBank function from AudioBank module
                    print("Audio bank saved.") #Save message
                
                elif key in key_sample_map: #If key is in the key_sample_map
                
                    sample = key_sample_map[key] #Get the corresponding sample
                    ac.play(sample) #Play the sample using AudioControls module
                
                else: #Else
                
                    print(f"Key '{key}' not mapped to any sample.") #Invalid key message

    #End FingerDrum

    def StepSeq(self, sound): #Start function stepseq with sound parameter

        # Step Sequencer: 4/4 x pattern, 16 steps, each step can trigger a sample
        slots_tuple = ac.load(sound) # Load samples using AudioControls module
        slots = slots_tuple[0] #Convert the sample tuple to a list

        num_steps = 16 #Number of steps in the sequencer
        sequences = {}  # Index to multiple seq, ej: {'A': [...], 'B': [...]}
        current_seq = 'A' #Sequence currently being edited
        sequences[current_seq] = [[] for _ in range(num_steps)] #Start with A empty sequence
        tempo = 120  # Default tempo in BPM

        sleep(1) #Sleep 1 seconds

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        
        print("\tStep Sequencer Mode") #Title message
        print("Assign samples to steps (1-16).") #Instructions assign samples
        print("Type 'play [seqs]' to play sequences, 'loop [seqs]' to loop [seqs], 'show' to display, 'clear' to reset, 'tempo [tempo]' to change tempo\n'seq [seq]' to change or create a sequence, 'save [name]' to save patterns, 'load [name]' to load patterns, 'q' to quit.") #Command instructions
        print("To assign multiple samples to a step: step# sample# sample# ... (e.g., 1 2 3 4)") #Assign multiple samples instruction
        print("Example to change or create a sequence: seq B") #To change sequence example
        
        while True: #Infinite loop for step sequencer commands
            
            cmd = input(f"[Sequence {current_seq}] Command (step# sample# (sample#), play, loop, show, clear, tempo, seq, save, load, q): ").strip() #Input command

            if cmd == 'q': #If command is 'q'
                
                print("Exiting Step Sequencer Mode.") #Exit message
                break #Break the loop

            elif cmd.startswith('play'): #If command starts with 'play'
                
                parts = cmd.split() #Split command
                seqs_to_play = [] #List of sequences

                if len(parts) == 1: #If no args
                
                    seqs_to_play = [current_seq] #Play current
                
                else: #If args
                
                    for s in parts[1:]: #Iterate args
                
                        s_upper = s.upper() #Upper case
                
                        if s_upper in sequences: #If exists
                
                            seqs_to_play.append(s_upper) #Add to list
                
                        else: #If not exists
                
                            print(f"Sequence '{s}' not found. Skipping.") #Print skip
                
                if not seqs_to_play: #If empty
                
                    print("No valid sequences to play.") #Print error
                
                    continue #Continue loop

                print(f"Playing sequences {seqs_to_play} at {tempo} BPM...") #Play message
                beat_duration = 60 / tempo  # seconds per beat
                step_duration = beat_duration / 4  # 16th note = quarter note / 4

                for seq in seqs_to_play: #Iterate sequences
                
                    print(f"Sequence {seq}:") #Print sequence name
                
                    for i, sample_idxs in enumerate(sequences[seq]): #Iterate over the sequence
                
                        print(f"Step {i+1}: ", end='') #Print current step
                
                        if sample_idxs: #If there are samples assigned to this step
                
                            print(f"Playing samples {sample_idxs}") #Print playing samples message
                
                            for sample_idx in sample_idxs: #Play all samples assigned to this step
                
                                if sample_idx < len(slots) and slots[sample_idx] is not None: #If sample index valid
                
                                    ac.play(slots[sample_idx]) #Play the sample
                
                        else: #Else
                
                            print("No samples") #Print no samples message
                
                        sleep(step_duration) #Wait for the duration of the step

            elif cmd.startswith('loop'): #If command starts with 'loop'
                
                parts = cmd.split() #Split command
                seqs_to_play = [] #List of sequences

                if len(parts) == 1: #If no args
                
                    seqs_to_play = [current_seq] #Loop current
                
                else: #If args
                
                    for s in parts[1:]: #Iterate args
                
                        s_upper = s.upper() #Upper case
                
                        if s_upper in sequences: #If exists
                
                            seqs_to_play.append(s_upper) #Add to list
                
                        else: #If not exists
                
                            print(f"Sequence '{s}' not found. Skipping.") #Print skip
                
                if not seqs_to_play: #If empty
                
                    print("No valid sequences to loop.") #Print error
                
                    continue #Continue loop

                print(f"Looping sequences {seqs_to_play} at {tempo} BPM...") #Play message
                print("Press Ctrl+C to stop looping.") #Loop info message
                
                beat_duration = 60 / tempo  # seconds per beat
                step_duration = beat_duration / 4  # 16th note = quarter note / 4

                try: #Try block to allow stopping with Ctrl+C
                
                    while True: #Loop forever until interrupted
                
                        for seq in seqs_to_play: #Iterate sequences
                            print(f"Sequence {seq}:") #Print sequence name
                            for i, sample_idxs in enumerate(sequences[seq]): #Iterate over the sequence
                
                                print(f"Step {i+1}: ", end='') #Print current step
                
                                if sample_idxs: #If there are samples assigned to this step
                
                                    print(f"Playing samples {sample_idxs}") #Print playing samples message
                
                                    for sample_idx in sample_idxs: #Play all samples assigned to this step
                
                                        if sample_idx < len(slots) and slots[sample_idx] is not None: #If sample index valid
                
                                            ac.play(slots[sample_idx]) #Play the sample
                                else: #Else
                
                                    print("No samples") #Print no samples message
                
                                sleep(step_duration) #Wait for the duration of the step
                
                except KeyboardInterrupt: #Catch Ctrl+C to exit loop
                    
                    print("\nStopped looping playback.") #Stop message

            elif cmd == 'show': #If command is 'show'
                
                for i, sample_idxs in enumerate(sequences[current_seq]): #Iterate over the sequence
                
                    if sample_idxs:
                
                        print(f"Step {i+1}: {sample_idxs}") #Print step and sample numbers
                
                    else:
                
                        print(f"Step {i+1}: None") #Print step and None

            elif cmd == 'clear': #If command is 'clear'
                
                sequences[current_seq] = [[] for _ in range(num_steps)] #Reset the sequence to empty lists
                print(f"Sequence '{current_seq}' cleared.") #Clear message

            elif cmd.startswith('tempo'): #If command start with 'tempo'
                
                try: #Try block to change tempo
                
                    _, new_tempo = cmd.split() #Split command to get new tempo
                    new_tempo = int(new_tempo) #Convert new tempo to integer
                
                    if new_tempo > 0: #If new tempo is positive
                
                        tempo = new_tempo #Set the new tempo
                        print(f"Tempo set to {tempo} BPM.") #Set tempo message
                
                    else: #Else
                
                        print("Tempo must be positive.") #Invalid tempo message
                
                except Exception: #Except block for invalid tempo command
                
                    print("Invalid command format. Use: tempo BPM") #Invalid command message

            elif cmd.startswith('seq'): #If command is 'seq'
                
                try: #Try block to change or create sequence
                
                    _, seq_name = cmd.split() #Get sequence name
                    seq_name = seq_name.upper() #Convert to uppercase
                
                    if seq_name not in sequences: #If sequence not exists
                
                        sequences[seq_name] = [[] for _ in range(num_steps)] #Create new sequence
                        print(f"Seq '{seq_name}' Created y selected.") #Created message
                
                    else: #Else
                
                        print(f"Seq '{seq_name}' Selected.") #Selected message
                
                    current_seq = seq_name #Set current sequence
                
                except Exception: #Catch exception
                    
                    print("Format: seq Name") #Invalid format message

            elif cmd.startswith('save'): #If command starts with 'save'
                
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
                        
                        data = {
                            "tempo": tempo,
                            "sequences": sequences
                        }
                        
                        with open(filename, 'w') as f: #Open file
                            json.dump(data, f, indent=4) #Dump json
                            
                        print(f"Patterns saved successfully to {filename}") #Success message
                    
                    else:
                        print("Save cancelled.")
                    
                except Exception as e: #Catch errors
                    
                    print(f"Error saving patterns: {e}") #Error message

            elif cmd.startswith('load'): #If command starts with 'load'
                
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
                                
                        print(f"Patterns loaded successfully from {filename}") #Success message
                    
                    else:
                        print("Load cancelled.")
                    
                except Exception as e: #Catch errors
                    
                    print(f"Error loading patterns: {e}") #Error message

            else: #else
                
                # Assign samples to step: format "step# sample# [sample# ...]"
                
                try: #Try block to assign samples to step
                
                    parts = cmd.split() #Split command
                    step = int(parts[0]) - 1 #Convert step to integer and adjust for 0-based index
                    sample_idxs = [int(idx) for idx in parts[1:]] #Convert all sample indices to integers
                
                    if 0 <= step < num_steps and all(0 <= idx < len(slots) for idx in sample_idxs): #If step and all sample indices are valid
                
                        sequences[current_seq][step] = sample_idxs #Assign list of samples to the step
                        print(f"Assigned samples {sample_idxs} to step {step+1} in sequence '{current_seq}'") #Assign message
                
                    else: #Else
                
                        print("Invalid step or sample index.") #Invalid index message
                
                except Exception: #Except block for invalid assign command
                
                    print("Invalid command format. Use: step# sample# [sample# ...]") #Invalid command message
         
    #End StepSeq