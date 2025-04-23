"""

This file controls the Audio banks for the Sampling proyect

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

class AudioBank:

    DEFAULT_BANK_PATH = "/home/elcalak/Repositorys/elcalak/Sampling/AudioBanks/Default"

    def __init__(self, name="DefaultBank"):

        self.name = name
        self.base_path = AudioBank.DEFAULT_BANK_PATH

        self._sounds = {}

        for i in range(1,10):
            
            placeholder_path = os.path.join(self.base_path, f"slot{i}.wav")
            self._sounds[i] = placeholdername

