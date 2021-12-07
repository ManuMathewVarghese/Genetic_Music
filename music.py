import sys
from midiutil.MidiFile import MIDIFile


time = 0
volume = 100
tempo = 120


def setInstruments(instr_list) -> int:
    '''
    A function to set channels for each instrument
    '''
    print(instr_list)
    numInstruments = len(instr_list) - 1
    if numInstruments <= 9:
        global track
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
    print("-----------------------------------------------")
    for line in args:
        print(line)
        channel = line[0]
        pitch = line[1]
        time = line[2]
        duration = line[3]
        print(channel,pitch,time,duration)
        track.addNote(0, channel, pitch, time, duration, volume)
    with open("output.mid", 'wb') as outFile:
        track.writeFile(outFile)

def musicGenerator(*args):
    setInstruments(args[0])
    musicEngine(args[1])


# a = [1, 27, 41]
# b = [[ 1,         54   ,       6.41902587 , 0.33824194],
#  [ 0  ,       62   ,       1.53410186 , 1.56861003],
#  [ 0  ,       55  ,        4.79133071,  2.46433114],
#  [ 0     ,    55     ,     3.45191166 , 0.35755675]]
# musicGenerator(a,b)