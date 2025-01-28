
from machine import Pin



led = Pin('LED', Pin.OUT)
led_state=""

while True:
    a = int(input("1-Zapnuto 0-Vypnuto "))
    if a == 0:
        led.value(0)
    else:
        led.value(1)



