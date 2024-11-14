import time
from machine import Pin
from time import sleep

time.sleep(0.1)
cervena = Pin(0, Pin.OUT)
zluta = Pin(1, Pin.OUT)
zelena = Pin(2, Pin.OUT)
button = Pin(20, Pin.IN, Pin.PULL_UP)
prechodbad = Pin(12, Pin.OUT)
prechodgut = Pin(13, Pin.OUT)
zmacknuti = False

def semafor():
    global zmacknuti
    while True:
        if zmacknuti:
            break
        else:
            cervena.value(1)
            for i in range(10):
                if button.value() == 0:
                    zmacknuti = True
                sleep(0.1)
            cervena.value(0)
            zluta.value(1)
            for i in range(10):
                if button.value() == 0:
                    zmacknuti = True
                sleep(0.1)
            zluta.value(0)
            zelena.value(1)
            for i in range(10):
                if button.value() == 0:
                    zmacknuti = True
                sleep(0.1)
            zelena.value(0)
            zluta.value(1)
            for i in range(10):
                if button.value() == 0:
                    zmacknuti = True
                sleep(0.1)
            zluta.value(0)

def prechod():
    global zmacknuti
    while True:
        zmacknuti = False
        prechodgut.value(0)
        prechodbad.value(1)
        semafor()
        prechodbad.value(0)
        prechodgut.value(1)
        cervena.value(1)
        sleep(5)
        for i in range(2):
            prechodgut.value(0)
            sleep(0.5)
            prechodgut.value(1)
            sleep(0.5)
        cervena.value(0)

prechod()