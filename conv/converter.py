import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input", type=str,
                    help="input file. Must end with \".sm\"", required=True)
parser.add_argument("-t", "--title", type=str,
                    help="track title", default="Unknown track")
parser.add_argument("-d", "--tempo", type=float,
                    help="track tempo", default=0.1)
args = parser.parse_args()

in_filename = args.input
out_filename = args.input.removesuffix(".sm") + ".json"

with open(in_filename, "r") as f:
    in_data = f.read()

sm_fragments = in_data.split("\n\n")
tones = []

for fragment in sm_fragments:
    octave_strings = fragment.split("\n")
    octave_strings = [o.removeprefix("RH:").removeprefix("LH:") for o in octave_strings]
    octaves = [(int(o[0]), o[1:].strip("|")) for o in octave_strings if o]

    for note in range(26):
        note_processed = False
        for octave in octaves:
            note_symbol = octave[1][note]
            if not note_symbol == "-":
                note_processed = True
                if note_symbol.isupper():
                    tones.append(note_symbol + "S" + str(octave[0]))
                else:
                    tones.append(note_symbol.upper() + str(octave[0]))
                break
        if not note_processed:
            tones.append("P")

with open(out_filename, "w") as f_out:
    json.dump({
        "title": args.title,
        "tempo": args.tempo,
        "format": "JSONg-a",
        "tones": tones
    }, f_out, indent=4, sort_keys=True)
