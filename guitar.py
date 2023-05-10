import json
import random

#parallel_keys = open('parallel_keys.json')
#parallel_keys = json.load(parallel_keys)

#relative_keys = open('relative_keys.json')
#relative_keys = json.load(relative_keys)

#minor_scales = open('minor_scale.json')
#minor_scales = json.load(minor_scales)

#ionian_scales = open('ionian_scale.json')
#ionian_scales = json.load(ionian_scales)

#dorian_scales = open('dorian_scale.json')
#dorian_scales = json.load(dorian_scales)

#phrygian_scales = open('phrygian_scale.json')
#phrygian_scales = json.load(phrygian_scales)


def fretboard_memorization():
  fretstrings = open('fret_strings.json')
  fretstrings = json.load(fretstrings)
  a = random.choice(list(fretstrings))
  print("      ", a)
  for value in fretstrings[a]:
    print("On string:", value['String'], "fret:", value['Fret'])

  start()

def get_triad():
  triads = open('triads.json')
  triads = json.load(triads)
  fretstrings = open('fret_strings.json')
  fretstrings = json.load(fretstrings)
  a = random.choice(list(triads))
  print(a)
  for value in triads[a]:
    print(value)
    for y in fretstrings[value]:
      print(y)

  start()

def get_specific_triad(note):
  triads = open('triads.json')
  triads = json.load(triads)
  for value in [triads(note)]:
    print(value)


def study_triad():
  triads = open('triads.json')
  triads = json.load(triads)
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
  triads = open('triads.json')
  triads = json.load(triads)
  fretstrings = open('fret_strings.json')
  fretstrings = json.load(fretstrings)
  a = input("Chord? ")
  print("This Chord")
  for value in triads[a]:
    print(value)
    for y in fretstrings[value][3:6]:
      print("String:", y['String'], "Fret:", y['Fret'])

  start()

def triads_in_major_scale():
  triads = open('triads.json')
  triads = json.load(triads)
  major_scales = open('major_scale.json')
  major_scales = json.load(major_scales)
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
  start()
