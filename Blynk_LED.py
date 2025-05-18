import network
import time
from machine import Pin
from blynklib_mp import Blynk

# Wi-Fi přihlašovací údaje
ssid = 'SPSELIT-host'
password = 'SPS20Ges23T*'

# Blynk Auth Token
auth_token = 'vvv0adhdw1TPtMBMQCqwWzG_gdIbUEkT'

# Připojení k Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(1)

print('Připojeno k Wi-Fi')

# Inicializace Blynk
blynk = Blynk(auth_token)

# Definujte handler pro virtuální pin
@blynk.virtual_write(1)
def v1_write_handler(value):
    print('V1:', value)
    if int(value[0]) == 1:
        led.on()
    else:
        led.off()

# Nastavení LED
led = Pin(2, Pin.OUT)

# Spuštění Blynk
while True:
    blynk.run()
