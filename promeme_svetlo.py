import time
from machine import Pin,PWM



switch = Pin(20, Pin.IN, Pin.PULL_UP)
svetilko = Pin(15, Pin.OUT)
svetilko1 = PWM(Pin(15))



i = 2


def nastaveni(i):
    global svetilko
    global svetilko1
    if i == 0:
        svetilko.value(0)
    elif i == 1:
        svetilko.value(1)
    elif i == 2:
       svetilko1
       svetilko.freq(1000)
       
          for cyklus_kroku in range(0, 65536, 1): 
            svetilko.duty_u16(cyklus_kroku)
          for cyklus_kroku in range(65536, 0, -1):
            svetilko.duty_u16(cyklus_kroku)
    
       
nastaveni(i)


while True:
    # vyzkoušet interrupt
    Pin.irq