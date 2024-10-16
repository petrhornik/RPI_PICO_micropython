from machine import Pin
from neopixel import NeoPixel
from time import sleep

RGBled = Pin(28, Pin.OUT)
Barva = NeoPixel(RGBled, 8)


while True:
    Barva[0] = (255, 0, 0)
    Barva.write()
    sleep(1)
    Barva[0] = (0, 255, 0)
    Barva.write()
    sleep(1)
    Barva[0] = (0, 0, 255)
    Barva.write()
    sleep(1)

