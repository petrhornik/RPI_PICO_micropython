from machine import Pin, PWM
from time import sleep

led = PWM(Pin(9))
push_button = Pin(20, Pin.IN)
led.freq(1000)

a = 1

def pricitani(pin):
    global a
    a = a + 1
    print("Funguje", a)
    if a > 4:
        a = 1

def led_0():
    global led
    led.duty_u16(0)

def led_100():
    global led
    led.duty_u16(65536)
    
def led_blik1():
    global led
    kroky = 1
    for cyklus_kroku in range(0, 65536, kroky): 
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)
    
    for cyklus_kroku in range(65536, 0, -kroky):
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)

def led_blik2():
    global led
    kroky = 5
    for cyklus_kroku in range(0, 65536, kroky): 
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)
    
    for cyklus_kroku in range(65536, 0, -kroky):
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)


push_button.irq(trigger=Pin.IRQ_FALLING, handler=pricitani)

while True:
    if a == 1:
        led_0()
    elif a == 2:
        led_100()
    elif a == 3:
        led_blik1()
    elif a == 4:
        led_blik2()
    
