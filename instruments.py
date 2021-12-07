#https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
instrumentList = {
"Acoustic Grand Piano": 1,
"Bright Acoustic Piano" : 2,
"Electric Grand Piano" : 3,
"Honky-tonk Piano" : 4,
"Electric Piano 1" : 5,
"Electric Piano 2" : 6,
"Harpsichord" : 7,
"Clavi" : 8,
"Celesta" : 9,
"Glockenspiel" : 10,
"Music Box" : 11,
"Vibraphone" : 12,
"Marimba" : 13,
"Xylophone" : 14,
"Tubular Bells" : 15,
"Dulcimer" : 16,
"Drawbar Organ" : 17,
"Percussive Organ" : 18,
"Rock Organ" : 19,
"Church Organ" : 20,
"Reed Organ" : 21,
"Accordion" : 22,
"Harmonica" : 23,
"Tango Accordion" : 24,
"Acoustic Guitar (nylon)" : 25,
"Acoustic Guitar (steel)" : 26,
"Electric Guitar (jazz)" : 27,
"Electric Guitar (clean)" : 28,
"Electric Guitar (muted)" : 29,
"Overdriven Guitar" : 30,
"Distortion Guitar" : 31,
"Guitar harmonics" : 32,
"Acoustic Bass" : 33,
"Electric Bass (finger)" : 34,
"Electric Bass (pick)" : 35,
"Fretless Bass" : 36,
"Slap Bass 1" : 36,
"Slap Bass 2" : 38,
"Synth Bass 1" : 39,
"Synth Bass 2" : 40,
"Violin" : 41,
"Viola" : 42,
"Cello" : 43,
"Contrabass" : 44,
"Tremolo Strings" : 45,
"Pizzicato Strings" : 46,
"Orchestral Harp" : 47,
"Timpani" : 48,
"String Ensemble 1" : 49,
"String Ensemble 2" : 50,
}

def showList():
    for key,value in instrumentList.items():
        print(value,"-",key)