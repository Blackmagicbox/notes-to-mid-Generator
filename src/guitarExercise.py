import mido 

class GuitarExercise:
    
    def __init__(self, name, notes):
        self.name = name
        self.notew = notes
        
    def file_name(self):
        exercise_filename = f"{self.name}.mid"
        return exercise_filename
    
    # Define a function that generates a MIDI file for a given exercise 
    def generate_mid_file(exercise):
        # Create a MIDI file object
        midi_file = mido.MidiFile()
        
        # Add a track to the MIDI file
        track = mido.MidiTrack()
        midi_file.tracks.append(track)
        
        # Set tempo to 120 bpm
        tempo = mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))
        track.append(tempo)
        
        
        # Generate MDI events for each note in the exercise
        for note, fret in exercise.items():
            # Create a NoteOn message for the current note
            note_on = mido.Message('note_on', note=note, velocity=127)
            track.append(note_on)
            
            # Create a NoteOff message for the current note
            delay = mido.second2tick(1, midi_file.ticks_per_beat())
            note_off = mido.Message('note_off', note=note, velocity=127)
            track.append(note_off)
            
            
        # Save the MIDI file
        filename = exercise.get_fileName()
        midi_file.save(filename)
        
        
    
    