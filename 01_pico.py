from time import sleep
from machine import Pin

led = Pin(8, Pin.OUT)    # 1 number in is Output
push_button = Pin(20, Pin.IN)  # 20 number pin is input

while True:
  
  logic_state = push_button.value()
  if logic_state == True:     # if push_button pressed
      led.value(0)           # led will turn ON
  else:                      # if push_button not pressed
      led.value(1)             # led will turn OFF
      sleep(10)