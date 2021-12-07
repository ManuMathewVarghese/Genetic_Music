import random

from midiutil.MidiFile import MIDIFile
# create your MIDI object
mf = MIDIFile(2)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 1
volume = 100
for i in range(0,10):
    mf.addProgramChange(0, 1, i, 50)
    pitch = random.randint(25,75)          # C4 (middle C)
    time = i             # start on beat 0
    duration = random.randint(1,6)         # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)

    print(pitch)

# pitch = 56           # E4
# time = 1             # start on beat 2
# duration = 1        # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)
#
# mf.addProgramChange(0,1,3,35)
#
# pitch = 56           # E4
# time = 3             # start on beat 2
# duration = 1        # 1 beat long
# mf.addNote(0, 1, pitch, time, duration, volume)


# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)