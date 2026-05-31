"""

This file controls the Play modes for the Sampling proyect

Created by:

Calak de Astora gh: https://github.com/elcalak

Suggest:
Compile in environment: Use Environment.sh to install all dependencies 
This file needs tk pack for work if you dont have this pack use (in Arch): sudo pacman -S tk

"""

import os #Import os library
from time import sleep #From module time import sleep function
import time #Import time module
import sys #Call sys module
import termios #Call termios module
import tty #Call tty module
import tkinter as tk #Call tkinter module
from tkinter import filedialog #Call filedialog module
from rich.console import Console #Call console module from rich library
import audio_bank as ab #Call the module from Control audio banks
import audio_controls as ac #Call the module from Control audio
import step_seq_controls as StepSC #Call the module to control Step Sequencer


class PlayModes:

    """
    This class contains the play modes that the proyect uses, right now
    has the finger drumming and the step sequencer. This modules needs a
    Audio Bank created to play correctly, without and Audio Bank this module
    will not work.
    It

    """

    def __init__(self): #Init contructor for PlayModes

        print("PlayModes initialized") #Work check

        #sleep(1) #Sleep 1 second
        os.system('clear' if os.name == 'posix' else 'cls') #Clear the terminal screen

    #End contructor

    def finger_drum(self, sound): #Start function fingerdrum with sound parameter

        """
        This mode emulates a finger drumming machine, using the keyboard as a
        interface to trigger the sounds. Needs and Audio Bank to work and load
        the sounds to the keyboard keys.

        """

        #***This function will be change for Micros***"

        console = Console() #Create a console object from rich library for better terminal output

        key_sample_map = {} #Create a dictionary to map keys to samples

        slots_tuple = ac.load(sound) # Load samples using AudioControls module
        slots = slots_tuple[0] #Convert the sample tuple to a list

        key_map_index = ['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n'] #Create a Index for keys

        for i in range(1, 10): # Map keys to sample names or indices

            key = key_map_index[i - 1] #Get the corresponding key from the index

            if i < len(slots) and slots[i] is not None: #Verify to slot exist

                key_sample_map[key] = slots[i]  # Map key to the corresponding sample
                print(f"Key '{key}' mapped to sample '{slots[i]}'") #Succes message

            else: #Else

                key_sample_map[key] = None  # No sample loaded for this slot
                print(f"Key '{key}' has no sample loaded.") #Info Message

        print("Mapping Succes!") #Work check line

        #sleep(1) #Sleep 1 seconds

        console.clear() #Clear the terminal screen

        title = r"""

███████╗██╗███╗   ██╗ ██████╗ ███████╗██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗ ████║██║
█████╗  ██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝██║  ██║██████╔╝██║   ██║██╔████╔██║██║
██╔══╝  ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║╚═╝
██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║██╗
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝

                """

        #Print rule with rich library
        console.rule(title = "You are in: Finger Drummin Mode", characters = "=")
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        #Print rule with rich library
        console.rule(title = "Back to: Playit Menu", characters = "=")

        console.print("Press keys ([bold blue]r ,t ,y ,f ,g ,h ,v ,n[/bold blue] " \
        "to play slot 1 to 9 respected) to play samples. " \
        "Press 'q' to quit, 'e' to start/stop recording, " \
        "and 's' to save bank.") #Instructions message

        is_recording = False #Recording state
        session_events = [] #List to store session events
        start_time = 0 #Start time of recording

        #Function to get a single character from standard input without echoing to the screen
        def getch():

            fd = sys.stdin.fileno() #Get the file descriptor for standard input
            old_settings = termios.tcgetattr(fd) #Save the current terminal settings

            try: #Init try

                tty.setraw(fd) #Set the terminal to raw mode
                ch = sys.stdin.read(1) #Read a single character

            finally: #Finally

                #Restore the terminal settings
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            return ch #Return the character read

        while True: #Infinite loop to capture key presses

            key = getch() #Get a single character input

            if key == 'q': #If key is 'q'

                print("Exiting Finger Drumming Mode.") #Exit message
                break #Break the loop

            if key == 'e':

                if not is_recording: #If not recording

                    is_recording = True #Start recording
                    start_time = time.time() #Set start time
                    session_events = [] #Reset events

                    print("Recording session started... Press 'e' to stop.") #Start message

                else: #If recording

                    is_recording = False #Stop recording
                    print("Recording session stopped.") #Stop message

                    if session_events: #If events recorded

                        root = tk.Tk() #Create Tk
                        root.withdraw() #Hide
                        filename = filedialog.asksaveasfilename(
                        title="Export Session WAV", defaultextension=".wav", filetypes=[
                        ("WAV files", "*.wav")
                        ]) #Ask filename
                        root.destroy() #Destroy Tk

                        if filename: #If filename

                            ac.export_session_wav(filename, session_events, sound) #Export

                        else:

                            print("No events to save.") #No events message

            elif key == 's': #If key is 's'

                ab.AudioBank().save_bank()  # Call SaveBank function from AudioBank module
                print("Audio bank saved.") #Save message

            elif key in key_sample_map: #If key is in the key_sample_map

                sample = key_sample_map[key] #Get the corresponding sample
                ac.play(sample) #Play the sample using AudioControls module

                if is_recording: #If recording

                    idx = key_map_index.index(key) + 1 #Get slot index
                    offset = time.time() - start_time #Calculate offset
                    session_events.append((offset, idx)) #Add event

            else: #Else

                print(f"Key '{key}' not mapped to any sample.") #Invalid key message

    #End FingerDrum

    def step_seq(self, sound): #Start function stepseq with sound parameter

        """
        A 16-step sequencer that allows assigning samples to steps for creating patterns.

        """

        console = Console() #Create a console object from rich library for better terminal output

        # Step Sequencer: 4/4 x pattern, 16 steps, each step can trigger a sample
        slots_tuple = ac.load(sound) # Load samples using AudioControls module
        slots = slots_tuple[0] #Convert the sample tuple to a list

        num_steps = 16 #Number of steps in the sequencer
        sequences = {}  # Index to multiple seq, ej: {'A': [...], 'B': [...]}
        current_seq = 'A' #Sequence currently being edited
        sequences[current_seq] = [[] for _ in range(num_steps)] #Start with A empty sequence
        tempo = 120  # Default tempo in BPM
        last_chain = [] # Variable to store the last played chain

        step_controls = StepSC.StepSeqControls() #Create StepSeqControls instance

        #sleep(1) #Sleep 1 seconds

        console.clear() #Clear the terminal screen

        title = r"""

███████╗████████╗███████╗██████╗ ███████╗███████╗ ██████╗ ██╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗██║
███████╗   ██║   █████╗  ██████╔╝███████╗█████╗  ██║   ██║██║
╚════██║   ██║   ██╔══╝  ██╔═══╝ ╚════██║██╔══╝  ██║▄▄ ██║╚═╝
███████║   ██║   ███████╗██║     ███████║███████╗╚██████╔╝██╗
╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚══════╝╚══════╝ ╚══▀▀═╝ ╚═╝

            """

        #Print rule with rich library
        console.rule(title = "You are in: Step Sequencer Mode", characters = "=")
        console.print(title, style="bold blue", justify="center") #Print title with rich style
        #Print rule with rich library
        console.rule(title = "Back to: Playit Menu", characters = "=")

        console.print("Assign samples to steps (1-16).") #Instructions assign samples
        console.print("Type 'play (seqs)' to play sequences, 'loop (seqs)' to loop seqs," \
                    "\n'show' to display, 'clear' to reset, 'tempo (tempo)' to change tempo" \
                    "\n'seq (seq)' to change or create a sequence, 'save (name)' to save patterns" \
                    "\n'load (name)' to load patterns," \
                    "\n'export (seqs)' to export wav, 'q' to quit.") #Command instructions
        console.print(
        "To assign multiple samples to a step: 'step# sample# sample#' ... (e.g., 1 2 3 4)"
        ) #Assign multiple samples instruction
        console.print("Example to change or create a sequence: 'seq B'") #To change sequence example

        console.rule(title = "Back to: Playit Menu", characters = "=") #Print rule with rich library

        while True: #Infinite loop for step sequencer commands

            cmd = console.input(f"[[bold]Sequence[/bold] [bold blue]{current_seq}[/bold blue]] Command (step# sample# (sample#), play, loop, show, clear, tempo, seq, save, load, q): ").strip() #Input command

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

                            console.print(
                            f"Sequence '{s}' not found. Skipping.", style="bold red", justify="full"
                            ) #Print skip

                if not seqs_to_play: #If empty

                    console.print(
                    "No valid sequences to play.", style="bold", justify="full"
                    ) #Print error

                    continue #Continue loop

                last_chain = seqs_to_play # Update last chain
                console.print(f"Playing sequences [bold blue]{seqs_to_play}[/bold blue] at [bold green]{tempo}[/bold green] BPM...") #Play message
                beat_duration = 60 / tempo  # seconds per beat
                step_duration = beat_duration / 4  # 16th note = quarter note / 4

                for seq in seqs_to_play: #Iterate sequences

                    console.print(
                    f"[bold]Sequence[/bold] [bold blue]{seq}[/bold blue]:"
                    ) #Print sequence name

                    for i, sample_idxs in enumerate(sequences[seq]): #Iterate over the sequence

                        console.print(
                        f"[bold]Step[/bold] [bold blue]{i+1}[/bold blue]: ", end=''
                        ) #Print current step

                        if sample_idxs: #If there are samples assigned to this step

                            console.print(
                            f"[bold]Playing samples[/bold] [bold blue]{sample_idxs}[/bold blue]"
                            ) #Print playing samples message

                            for sample_idx in sample_idxs: #Play all samples assigned to this step

                                #If sample index valid
                                if sample_idx < len(slots) and slots[sample_idx] is not None:

                                    ac.play(slots[sample_idx]) #Play the sample

                        else: #Else

                            console.print("[bold]No samples[/bold]") #Print no samples message

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

                            console.print(
                            f"Sequence '{s}' not found. Skipping.", style="bold red", justify="full"
                            ) #Print skip

                if not seqs_to_play: #If empty

                    print("No valid sequences to loop.", style="bold") #Print error

                    continue #Continue loop

                last_chain = seqs_to_play # Update last chain
                console.print(f"Looping sequences [bold blue]{seqs_to_play}[/bold blue] at [bold green]{tempo}[/bold green] BPM...") #Play message
                console.print(
                "Press Ctrl+C to stop looping.",  style="bold red", justify="full"
                ) #Loop info message

                beat_duration = 60 / tempo  # seconds per beat
                step_duration = beat_duration / 4  # 16th note = quarter note / 4

                try: #Try block to allow stopping with Ctrl+C

                    while True: #Loop forever until interrupted

                        for seq in seqs_to_play: #Iterate sequences

                            console.print(
                            f"[bold]Sequence[/bold] [bold blue]{seq}[/bold blue]:"
                            ) #Print sequence name

                            #Iterate over the sequence
                            for i, sample_idxs in enumerate(sequences[seq]):

                                console.print(
                                f"[bold]Step[/bold] [bold blue]{i+1}[/bold blue]: ", end=''
                                ) #Print current step

                                if sample_idxs: #If there are samples assigned to this step

                                    console.print(f"[bold]Playing samples[/bold] [bold blue]{sample_idxs}[/bold blue]") #Print playing samples message

                                    #Play all samples assigned to this step
                                    for sample_idx in sample_idxs:

                                        #If sample index valid
                                        if sample_idx < len(slots) and slots[sample_idx] is not None:

                                            ac.play(slots[sample_idx]) #Play the sample
                                else: #Else

                                    #Print no samples message
                                    console.print("[bold]No samples[/bold]")

                                sleep(step_duration) #Wait for the duration of the step

                except KeyboardInterrupt: #Catch Ctrl+C to exit loop

                    console.print("\nStopped looping playback.", style="bold") #Stop message

            elif cmd == 'clear': #If command is 'clear'

                #Reset the sequence to empty lists
                sequences[current_seq] = [[] for _ in range(num_steps)]
                console.print(
                f"Sequence [bold blue]'{current_seq}'[/bold blue] cleared."
                ) #Clear message

            elif cmd == 'show': #If command is 'show'

                step_controls.show(sequences, current_seq)

            elif cmd.startswith('tempo'): #If command start with 'tempo'

                tempo = step_controls.tempo(cmd) #Call tempo function from StepSeqControls module

            elif cmd.startswith('seq'): #If command is 'seq'

                #Call Seq function from StepSeqControls module                
                sequences, current_seq = step_controls.seq(cmd, sequences, current_seq, num_steps)

            elif cmd.startswith('save'): #If command starts with 'save'

                #Call Save function from StepSeqControls module
                step_controls.save_patterns(tempo, sequences, last_chain)

            elif cmd.startswith('load'): #If command starts with 'load'

                #Call Load function and store in a temporary variable to handle cancellation (None return)
                loaded_data = step_controls.load_patterns()

                #If loaded_data exist
                if loaded_data:
                    
                    tempo, sequences, last_chain = loaded_data #Unpack loaded data into current state variables
                    
                    console.print(
                        "Patterns loaded successfully.", style="bold green"
                    ) #Success message
                
                else: #if loaded_data not exits (cancelled or failed)
                
                    # If load was cancelled or failed, we simply don't update the current state
                    console.print(
                        "Load cancelled or failed. Current patterns preserved.", style="bold red"
                    ) #Failure message

            elif cmd.startswith('export'): #If command starts with 'export'

                #Call export function
                step_controls.export(cmd, sequences, current_seq, tempo, sound, last_chain)

            else: #else

                # Assign samples to step: format "step# sample# [sample# ...]"

                try: #Try block to assign samples to step

                    parts = cmd.split() #Split command
                    step = int(parts[0]) - 1 #Convert step to integer and adjust for 0-based index
                    #Convert all sample indices to integers
                    sample_idxs = [int(idx) for idx in parts[1:]]

                    #If step and all sample indices are valid
                    if 0 <= step < num_steps and all(0 <= idx < len(slots) for idx in sample_idxs):

                        #Assign list of samples to the step
                        sequences[current_seq][step] = sample_idxs
                        console.print(f"Assigned samples [bold green]{sample_idxs}[/bold green] to step [bold magenta]{step+1}[/bold magenta] in sequence [bold blue]'{current_seq}'[/bold blue]") #Assign message

                    else: #Else

                        console.print(
                        "Invalid step or sample index.", style="bold") #Invalid index message

                except Exception: #Except block for invalid assign command

                    #Restore the terminal settings
                    console.print(
                    "Invalid command format. Use: step# sample# [sample# ...]", style="bold red")

    #End StepSeq
