from music21 import stream, chord, tempo
import pygame
import time

# Initialize pygame
pygame.init()

# Set the frequency and size of the audio buffer
pygame.mixer.pre_init(44100, -16, 2, 2048)

# Initialize the mixer module
pygame.mixer.init()

# Define the chord progression
chords = [
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
    [("C4", "E4", "G4"), 2],    # C major chord (2 beats)
    [("F4", "A4", "C5"), 2],    # F major chord (2 beats)
    [("E4", "G4", "B4"), 2],    # E minor chord (2 beats)
    [("A3", "C5", "E5"), 2],    # A minor chord (2 beats)
    [("D4", "F4", "A4"), 2],    # D minor chord (2 beats)
    [("G4", "B4", "D5"), 2],    # G major chord (2 beats)
]


# Create a new music21 Stream object
chord_stream = stream.Stream()

# Add chords to the Stream
for chord_notes, duration in chords:
    new_chord = chord.Chord(chord_notes, quarterLength=duration)
    chord_stream.append(new_chord)

# Set the tempo of the chord progression
chord_stream.append(tempo.MetronomeMark(number=120))

# Define the output MIDI file path
midi_file_path = "chord_progression.mid"

# Save the music21 Stream object as a MIDI file
chord_stream.write('midi', midi_file_path)

# Loop infinitely, playing the chord progression
while True:
    # Load the MIDI file using pygame
    pygame.mixer.music.load(midi_file_path)
    
    # Play the MIDI file
    pygame.mixer.music.play()
    
    # Wait for the duration of the chord progression before playing it again
    time.sleep(sum([duration for _, duration in chords]))

