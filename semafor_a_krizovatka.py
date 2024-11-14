from machine import Pin
from time import sleep

cervena = Pin(0, Pin.OUT)
zluta = Pin(1, Pin.OUT)
zelena = Pin(2, Pin.OUT)
button = Pin(20, Pin.IN)
prechodbad = Pin(12, Pin.OUT)
prechodgut = Pin(13, Pin.OUT)


def semafor():
        cervena.value(1)
        sleep(1)
        cervena.value(0)
        zluta.value(1)
        sleep(1)
        zluta.value(0)
        zelena.value(1)
        sleep(1)
        zelena.value(0)

def prechod():
    while True:
        if button.value() == 1:
            cervena.value(1)
            prechodbad.value(0)
            prechodgut.value(1)
        else:
            prechodgut.value(0)
            prechodbad.value(1)
            while button.value() == False:
                semafor()
            

prechod()