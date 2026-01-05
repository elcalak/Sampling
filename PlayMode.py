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
Compile in environment (in Arch): Environment/piplibs/bin/python
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
        slots_tuple = ac.load(sound)
        slots = slots_tuple[0]

        num_steps = 16
        sequence = [None] * num_steps  # Each step can hold a sample index
        tempo = 120  # Default tempo in BPM

        sleep(1) #Sleep 1 seconds

        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen
        
        print("\tStep Sequencer Mode") #Title message
        print("Assign samples to steps (1-16).") #Instructions assign samples
        print("Type 'play' to play the sequence, 'show' to display, 'clear' to reset, 'tempo' to change tempo, 'q' to quit.") #Command instructions

        while True: #Infinite loop for step sequencer commands
            
            cmd = input("Command (step# sample#, play, show, clear, tempo, q): ").strip() #Input command

            if cmd == 'q': #If command is 'q'
                
                print("Exiting Step Sequencer Mode.") #Exit message
                break #Break the loop

            elif cmd == 'play': #If command is 'play'
                
                print(f"Playing sequence at {tempo} BPM...") #Play message
                
                # Calculate the duration of a quarter note (beat)
                beat_duration = 60 / tempo  # seconds per beat
                # For a 16-step sequencer in 4/4, each step is a 16th note
                step_duration = beat_duration / 4  # 16th note = quarter note / 4

                for i, sample_idx in enumerate(sequence): #Iterate over the sequence
                    
                    print(f"Step {i+1}: ", end='') #Print current step
                    
                    if sample_idx is not None and sample_idx < len(slots) and slots[sample_idx] is not None: #If sample exist and slot is load
                    
                        print(f"Playing sample {sample_idx}") #Print playing sample message
                        ac.play(slots[sample_idx]) #Play the sample using AudioControls module
                    
                    else: #Else
                    
                        print("No sample") #Print no sample message
                    
                    sleep(step_duration) #Wait for the duration of the step

            elif cmd == 'show': #If command is 'show'
                
                for i, sample_idx in enumerate(sequence): #Iterate over the sequence
                
                    sample_name = slots[sample_idx] if sample_idx is not None and sample_idx < len(slots) else "None" #Get sample name or None
                    print(f"Step {i+1}: {sample_name}") #Print step and sample name

            elif cmd == 'clear': #If command is 'clear'
               
                sequence = [None] * num_steps #Reset the sequence
                print("Sequence cleared.") #Clear message

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

            else: #else

                # Assign sample to step: format "step# sample#"

                try: #Try block to assign sample to step

                    step_str, sample_str = cmd.split() #Split command to get step and sample
                    step = int(step_str) - 1 #Convert step to integer and adjust for 0-based index
                    sample_idx = int(sample_str) #Convert sample index to integer

                    if 0 <= step < num_steps and 0 <= sample_idx < len(slots): #If step and sample index are valid

                        sequence[step] = sample_idx #Assign sample to the step
                        print(f"Assigned sample {sample_idx} to step {step+1}") #Assign message

                    else: #Else

                        print("Invalid step or sample index.") #Invalid index message

                except Exception: #Except block for invalid assign command

                    print("Invalid command format. Use: step# sample#") #Invalid command message
        
    #End StepSeq