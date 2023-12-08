# Midi Generator

This is a simple Python script that generates a MIDI file from input notes and tempo values.

## Installation

To install the required packages, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages listed in the `requirements.txt` file.

## Usage

To use the script, you need to import the `MidiGenerator` class from the `midi_generator.py` script. Here is a basic example:

```python
from src.midi_generator import MidiGenerator

midi_gen = MidiGenerator()

notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
tempo = 120

midi_gen.get_notes(notes)
midi_gen.get_tempo(tempo)
midi_gen.generate_midi('output.mid')
```

In this example, the `get_notes` method takes a list of notes as input, the `get_tempo` method takes a tempo value as input, and the `generate_midi` method generates a MIDI file with the given notes and tempo.

## Running Tests

To run the tests, navigate to the project directory and run the following command:

```bash
python -m unittest tests/test_midi_generator.py
```

This will run all the unit tests defined in the `test_midi_generator.py` script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)