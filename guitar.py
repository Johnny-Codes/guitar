import json
import random

parallel_keys = open('parallel_keys.json')
parallel_keys = json.load(parallel_keys)

relative_keys = open('relative_keys.json')
relative_keys = json.load(relative_keys)

fretstrings = open('fret_strings.json')
fretstrings = json.load(fretstrings)

major_scales = open('major_scale.json')
major_scales = json.load(major_scales)


triads = {
  "C Major": ["C", "E", "G"],
  "C Minor": ["C", "Eb", "G"],
  "C Diminished 7th": ["C", "Eb", "G", "Bb"],
  "Cb 5": ["C", "Eb", "Gb"],
  "C# Major": ["C#", "F#", "A#"],
  "C# Minor": ["C#", "E", "G#"],
  "C# Diminished 7th": ["C#", "E", "G#", "B"],
  "C#b 5": ["C#", "E", "G"],
  "D Major": ["D", "F#", "A"],
  "D Minor": ["D", "F", "A"],
  "D Diminished 7th": ["D", "F", "G", "A#"],
  "Db 5": ["D", "F", "G"],
  "Eb Major": ["Eb", "G", "Bb"],
  "Eb Minor": ["Eb", "G", "Bb"],
  "Eb Diminished 7th": ["Eb", "G", "Bb", "Db"],
  "Ebb 5": ["Eb", "G", "B"],
  "E Major": ["E", "G#", "B"],
  "E Minor": ["E", "G", "B"],
  "E Diminished 7th": ["E", "G", "B", "D"],
  "Eb 5": ["E", "G", "Bb"],
  "F Major": ["F", "A", "C"],
  "F Minor": ["F", "Ab", "C"],
  "F Diminished 7th": ["F", "Ab", "C", "Eb"],
  "Fb 5": ["F", "Ab", "Cb"],
  "F# Major": ["F#", "A#", "C#"],
  "F# Minor": ["F#", "A", "C#"],
  "F# Diminished 7th": ["F#", "A", "C#", "E"],
  "F#b 5": ["F#", "A", "C"],
  "G Major": ["G", "B", "D"],
  "G Minor": ["G", "Bb", "D"],
  "G Diminished 7th": ["G", "Bb", "D", "F"],
  "Gb 5": ["G", "Bb", "Db"],
  "Ab Major": ["Ab", "C", "Eb"],
  "Ab Minor": ["Ab", "Cb", "Eb"],
  "Ab Diminished 7th": ["Ab", "Cb", "Eb", "Gb"],
  "Abb 5": ["Ab", "Cb", "E"],
  "A Major": ["A", "C#", "E"],
  "A Minor": ["A", "C", "E"],
  "A Diminished 7th": ["A", "C", "E", "G"],
  "Ab 5": ["A", "C", "Eb"],
  "Bb Major": ["Bb", "D", "F"],
  "Bb Minor": ["Bb", "C#", "F"],
  "Bb Diminished 7th": ["Bb", "C#", "F", "G#"],
  "Bbb 5": ["Bb", "C#", "E"],
  "B Major": ["B", "D#", "F#"],
  "B Minor": ["B", "D", "F#"],
  "B Diminished 7th": ["B", "D", "F#", "A"],
  "C Major 7th": ["C", "E", "G", "B"],
  "C Minor 7th": ["C", "Eb", "G", "Bb"],
  "C# Major 7th": ["C#", "F", "G#", "C"],
  "C# Minor 7th": ["C#", "E", "G#", "B"],
  "D Major 7th": ["D", "F#", "A", "C#"],
  "D Minor 7th": ["D", "F", "A", "C"],
  "D# Major 7th": ["D#", "G", "A#", "C#"],
  "D# Minor 7th": ["D#", "F#", "A#", "C"],
  "E Major 7th": ["E", "G#", "B", "D#"],
  "E Minor 7th": ["E", "G", "B", "D"],
  "F Major 7th": ["F", "A", "C", "E"],
  "F Minor 7th": ["F", "Ab", "C", "Eb"],
  "F# Major 7th": ["F#", "A#", "C#", "F"],
  "F# Minor 7th": ["F#", "B", "C#", "E"],
  "G Major 7th": ["G", "B", "D", "F#"],
  "G Minor 7th": ["G", "Bb", "D", "F"],
  "G# Major 7th": ["G#", "C", "D#", "G"],
  "G# Minor 7th": ["G#", "B", "D#", "F#"],
  "A Major 7th": ["A", "C#", "E", "G#"],
  "A Minor 7th": ["A", "C", "E", "G"],
  "A# Major 7th": ["A#", "D", "F", "A"],
  "A# Minor 7th": ["A#", "C#", "F", "G#"],
  "B Major 7th": ["B", "D#", "F#", "A#"],
  "B Minor 7th": ["B", "D", "F#", "A"]
}

minor_scales = {
    "A Minor": ["A", "B", "C", "D", "E", "F", "G"],
    "A# Minor": ["A#", "C", "C#", "D#", "F", "F#", "G#"],
    "B Minor": ["B", "C#", "D", "E", "F#", "G", "A"],
    "C Minor": ["C", "D", "D#", "F", "G", "G#", "A#"],
    "C# Minor": ["C#", "D#", "E", "F#", "G#", "A", "B"],
    "D Minor": ["D", "E", "F", "G", "A", "A#", "C"],
    "D# Minor": ["D#", "F", "F#", "G#", "A#", "B", "C#"],
    "E Minor": ["E", "F#", "G", "A", "B", "C", "D"],
    "F Minor": ["F", "G", "G#", "A#", "C", "C#", "D#"],
    "F# Minor": ["F#", "G#", "A", "B", "C#", "D", "E"],
    "G Minor": ["G", "A", "A#", "C", "D", "D#", "F"],
    "G# Minor": ["G#", "A#", "B", "C#", "D#", "E", "F#"]
}

ionian_scales = {
  "C Ionian": ["C", "D", "E", "F", "G", "A", "B"],
  "D Ionian": ["D", "E", "F#", "G", "A", "B", "C#"],
  "E Ionian": ["E", "F#", "G#", "A", "B", "C#", "D#"],
  "F Ionian": ["F", "G", "A", "Bb", "C", "D", "E"],
  "G Ionian": ["G", "A", "B", "C", "D", "E", "F#"],
  "A Ionian": ["A", "B", "C#", "D", "E", "F#", "G#"],
  "B Ionian": ["B", "C#", "D#", "E", "F#", "G#", "A#"]
}

dorian_scales = {
  "C Dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
  "C# Dorian": ["C#", "D#", "E", "F#", "G#", "A#", "B"],
  "D Dorian": ["D", "E", "F", "G", "A", "Bb", "C"],
  "D# Dorian": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
  "E Dorian": ["E", "F#", "G", "A", "B", "C", "D"],
  "F Dorian": ["F", "G", "Ab", "Bb", "C", "D", "Eb"],
  "F# Dorian": ["F#", "G#", "A", "B", "C#", "D#", "E"],
  "G Dorian": ["G", "A", "Bb", "C", "D", "Eb", "F"],
  "G# Dorian": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
  "A Dorian": ["A", "B", "C", "D", "E", "F", "G"],
  "A# Dorian": ["A#", "B#", "C#", "D#", "E#", "F#", "G#"],
  "B Dorian": ["B", "C#", "D", "E", "F#", "G", "A"],
}

phrygian_scales = {
  "C Phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
  "C# Phrygian": ["C#", "D", "E", "F#", "G#", "A", "B"],
  "Db Phrygian": ["Db", "Ebb", "Fb", "Gb", "Abb", "Bbb", "Cb"],
  "D Phrygian": ["D", "E", "F", "G", "A", "Bb", "C"],
  "D# Phrygian": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
  "Eb Phrygian": ["Eb", "Fb", "Gb", "Ab", "Bbb", "Cb", "Db"],
  "E Phrygian": ["E", "F", "G", "A", "Bb", "C", "D"],
  "F Phrygian": ["F", "Gb", "Ab", "Bb", "C", "Db", "Eb"],
  "F# Phrygian": ["F#", "G", "A", "B", "C#", "D", "E"],
  "Gb Phrygian": ["Gb", "Abb", "Bbb", "Cb", "Dbb", "Ebb", "Fb"],
  "G Phrygian": ["G", "A", "Bb", "C", "D", "Eb", "F"],
  "G# Phrygian": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
  "Ab Phrygian": ["Ab", "Bbb", "Cb", "Db", "Ebb", "Fb", "Gb"],
  "A Phrygian": ["A", "Bb", "C", "D", "Eb", "F", "G"],
  "A# Phrygian": ["A#", "B", "C#", "D#", "E", "F#", "G#"],
  "Bb Phrygian": ["Bb", "Cb", "Db", "Eb", "F", "Gb", "Ab"],
  "B Phrygian": ["B", "C", "D", "E", "F#", "G", "A"]
}


def fretboard_memorization():
    a = random.choice(list(fretstrings))
    print("      ", a)
    for value in fretstrings[a]:
        print("On string:", value['String'], "fret:", value['Fret'])

    start()

def get_triad():
    a = random.choice(list(triads))
    print(a)
    for value in triads[a]:
        print(value)
        for y in fretstrings[value]:
            print(y)

    start()

def get_specific_triad(note):
    for value in [triads(note)]:
        print(value)


def study_triad():
    a = random.choice(list(triads))
    print("These are the notes of the triad: ")
    for value in triads[a]:
        print(value)
    answer = input("What is the Triad? ")
    if answer == a:
        print("Correct")
    else:
        print(a)

    study_triad()

def top_three_triads():
    a = input("Chord? ")
    print("This Chord")
    for value in triads[a]:
        print(value)
        for y in fretstrings[value][3:6]:
            print("String:", y['String'], "Fret:", y['Fret'])

    start()

def triads_in_major_scale():
    a = random.choice(list(major_scales))
    print("These are the root notes in the", a, "scale")
    print(a)
    for notes in triads[a]:
        print(notes)
        get_triad(notes)

def start():
    print("What would you like to do")
    print("1: fretboard memorization")
    print("2: triad fingering")
    print("3: study triads")
    print("4: see the triad on the high 3 strings")
    answer = (input("Well? "))
    if answer == "1":
        fretboard_memorization()
    elif answer == "2":
        get_triad()
    elif answer == "3":
        study_triad()
    elif answer == "4":
        top_three_triads()

if __name__ == '__main__':
    print('Welcome to the guitar practice program')
    start()
