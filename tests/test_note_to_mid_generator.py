import unittest
import mido
import os
from src.guitarExercise import GuitarExercise, generate_mid_file

class TestGenerateMidFile(unittest.TestCase):
    def setUp(self):
        self.exercise = {
            60: 0,  # C4
            62: 1,  # D4
            64: 2,  # E4
        }
        self.filename = "test.mid"
        self.exercise.get_fileName = lambda: self.filename

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_generate_mid_file(self):
        generate_mid_file(self.exercise)

        # Check if the file was created
        self.assertTrue(os.path.exists(self.filename))

        # Load the MIDI file
        midi_file = mido.MidiFile(self.filename)

        # Check if the MIDI file has one track
        self.assertEqual(len(midi_file.tracks), 1)

        # Check if the first message is a 'set_tempo' message
        self.assertEqual(midi_file.tracks[0][0].type, 'set_tempo')

        # Check if the 'set_tempo' message has the correct tempo
        self.assertEqual(midi_file.tracks[0][0].tempo, mido.bpm2tempo(120))

        # Check if the MIDI file has the correct number of 'note_on' and 'note_off' messages
        note_on_messages = [msg for msg in midi_file.tracks[0] if msg.type == 'note_on']
        note_off_messages = [msg for msg in midi_file.tracks[0] if msg.type == 'note_off']
        self.assertEqual(len(note_on_messages), len(self.exercise))
        self.assertEqual(len(note_off_messages), len(self.exercise))

        # Check if the 'note_on' and 'note_off' messages have the correct notes
        for note, _ in self.exercise.items():
            self.assertTrue(any(msg.note == note for msg in note_on_messages))
            self.assertTrue(any(msg.note == note for msg in note_off_messages))

if __name__ == '__main__':
    unittest.main()