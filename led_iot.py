import time
import network
from machine import Pin
import blynklib
 
led=machine.Pin('LED', machine.Pin.OUT)
led.on()
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SPSELIT-host","SPS20Ges23T*")
 
BLYNK_AUTH = 'vvv0adhdw1TPtMBMQCqwWzG_gdIbUEkT'
 
# connect the network       
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
    
 
"Connection to Blynk"
# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
 
# Register virtual pin handler
@blynk.on("V0") #virtual pin V0
def v0_write_handler(value): #read the value
    if int(value[0]) == 1:
        led.value(1) #turn the led on        
    else:
        led.value(0)    #turn the led off
while True:
    blynk.run()
