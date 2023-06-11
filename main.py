from machine import Pin, PWM, mem32
from micropython import const
from os import listdir
from random import randrange

from tools import fs_stat
from basic_synth import BasicSynth

def random_shuffle(seq):
    l = len(seq)
    for i in range(l):
        j = randrange(l)
        seq[i], seq[j] = seq[j], seq[i]

led = Pin(25, Pin.OUT)

stat = fs_stat()
print(f"FS stat: {stat[0]} KiB available, {stat[1]} KiB free")

# check if whether rp2 is not connected to usb host
SIE_STATUS=const(0x50110000+0x50)
CONNECTED=const(1<<16)
if not (mem32[SIE_STATUS] & CONNECTED):
    try:
        buzzer = PWM(Pin(15))
        s = BasicSynth(buzzer, 0.1)
        led.value(1)
        track_files = listdir("songs")
        random_shuffle(track_files)
        for filename in track_files:
            s.play_jsong_file("/songs/" + filename)
    except Exception as e:
        with open("/log", "a") as f:
            f.write(str(e) + "\n")

