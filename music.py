import sys
from io import BytesIO
from midiutil.MidiFile import MIDIFile
import pygame.mixer
from time import sleep
import random
from datetime import datetime
time = 0
volume = 100
tempo = 138

# To assign each channel according to instrument.
def setInstruments(instr_list) -> None:
    '''
    A function to set channels for each instrument
    '''
    global numInstruments,track
    numInstruments = len(instr_list)
    if numInstruments <= 9:
        track = MIDIFile(1)
        track.addTempo(track, time, tempo)
        #Changing channels and assigning an instrument
        for channel,program in enumerate(instr_list):
            track.addProgramChange(0,channel,0,program)
    else:
        sys.exit("Sorry, currently supports only a maximum 9 instruments")

def musicEngine(args) -> None:
    '''
    A function to generate music from given values of pitch, time, duration of the instrument
    Pitch values are taken from "https://www.midi.org/specifications-old/item/gm-level-1-sound-set"
    '''
    #memFile = BytesIO()
    for line in args:
        channel = int(line[0])
        pitch = int(line[1])
        time = line[2]
        duration = line[3]
        track.addNote(0, channel, pitch, time, duration, volume)
    # track.writeFile(memFile)
    with open("track.mid","wb") as outfile:
        track.writeFile(outfile)
    pygame.init()
    pygame.mixer.init()
    #memFile.seek(0)
    pygame.mixer.music.load("track.mid")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)

# Function to generate music
def musicGenerator(*args):
    '''
    Setinstruments will create a track with channels
    music engine will generate notes
    '''
    setInstruments(args[0])
    musicEngine(args[1])

# A generator to generate random note
def random_note() -> list:
    channel = random.randint(0, numInstruments)
    pitch = random.randint(36, 96)
    time = random.randint(0, 20)
    duration = random.randint(1, 2)
    return [channel,pitch,time,duration]