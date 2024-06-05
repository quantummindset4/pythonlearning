from music21 import stream, note, chord, tempo

# Define the melody notes for Canon in D
melody_notes = [
    ("D5", 4), ("A4", 4), ("B4", 4), ("F#4", 4),
    ("G4", 4), ("D4", 4), ("G4", 4), ("A4", 4),
    ("D5", 4), ("A4", 4), ("B4", 4), ("F#4", 4),
    ("G4", 4), ("D4", 4), ("G4", 4), ("A4", 4),
    ("B4", 2), ("A4", 2), ("G4", 2), ("F#4", 2),
    ("G4", 2), ("A4", 2), ("B4", 2), ("D5", 2),
    ("F#5", 4), ("D5", 4), ("B4", 4), ("G4", 4),
    ("A4", 4), ("F#4", 4), ("G4", 4), ("D4", 4),
]

# Define the chord progression for Canon in D
chord_progression = [
    [("D4", "F#4", "A4"), 8],  # D major chord (2 beats)
    [("B3", "D4", "F#4"), 8],  # B minor chord (2 beats)
    [("G3", "B3", "D4"), 8],   # G major chord (2 beats)
    [("A3", "C#4", "E4"), 8],  # A major chord (2 beats)
]

# Create a new music21 Stream object
music_stream = stream.Stream()

# Add melody notes to the Stream
for note_name, duration in melody_notes:
    new_note = note.Note(note_name, quarterLength=duration)
    music_stream.append(new_note)

# Add chords to the Stream
for chord_notes, duration in chord_progression:
    new_chord = chord.Chord(chord_notes, quarterLength=duration)
    music_stream.append(new_chord)

# Set the tempo of the music
music_stream.append(tempo.MetronomeMark(number=72))

# Define the output MIDI file path
midi_file_path = "advanced_canon_in_d.mid"

# Save the music21 Stream object as a MIDI file
music_stream.write('midi', midi_file_path)

print("Advanced Canon in D MIDI file generated successfully.")

