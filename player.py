import json
from machine import PWM, Pin
from os import listdir
import json

from basic_synth import BasicSynth

class Player:
    def __init__(self, pwm_pin=15, drop_to_ui=True):
        self._pwm = PWM(Pin(pwm_pin))
        self._synth = BasicSynth(self._pwm)

        if drop_to_ui:
            try:
                self.ui()
            except KeyboardInterrupt:
                print("mkay.")

    def ui(self):
        print("Loading tracks info... One moment")
        track_files = listdir("songs")
        tracks = []

        for filename in track_files:
            with open("/songs/" + filename, "r") as file:
                title = json.load(file)["title"]
                tracks.append((filename.split(".")[0], title))

        while True:
            print("\n")
            for i, track in enumerate(tracks):
                print(f"[{i:2} {track[0]:14} -- {track[1]} ]")

            chosen_track = ""

            while chosen_track == "":
                choice = input("Make your choice (name or index) or [Q] to exit: ")
                try:
                    if choice in ("Q", "q"):
                        return
                    elif choice.isdigit():
                        chosen_track = tracks[int(choice)][0]
                    else:
                        chosen_track = [t for t in tracks if t[0] == choice][0][0]
                except IndexError:
                    print("Invalid choice.")
            
            self._synth.play_jsong_file("/songs/" + chosen_track + ".json")

        