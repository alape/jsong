from machine import Pin, PWM

from tools import fs_stat
from basic_synth import BasicSynth

led = Pin(25, Pin.OUT)
# buzzer = PWM(Pin(15))
# s = BasicSynth(buzzer, 0.1)
led.value(1)
# s.play_jsong_file("/e1m1.json")
# led.value(0)

stat = fs_stat()
print(f"FS stat: {stat[0]} KiB available, {stat[1]} KiB free")
