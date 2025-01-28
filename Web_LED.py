import network
import socket
from machine import Pin

# Připojení k Wi-Fi
ssid = 'SPSELIT-host'
password = 'SPS20Ges23T*'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('Připojeno k Wi-Fi:', wlan.ifconfig())

# Nastavení vestavěné LED
led = Pin('LED', Pin.OUT)
led_state=""

# Vytvoření webového serveru
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('IP adr. je:', addr) # IP adresa RPI

while True:
    cl, addr = s.accept()
    print('Připojeno od', addr) #vypíše IP adresu zařízení co interaguje s web rozhraním
    request = cl.recv(1024)
    request = str(request)
    print('Požadavek:', request) # vypisuje interakce ostatních zařízení s web. rozhranim

    if '/?led=on' in request:
        led.value(1)
        led_state = "YES"
        print(led_state)
    if '/?led=off' in request:
        led.value(0)
        led_state = "NO"
        print(led_state)

    response = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Ovládání LED</title>
</head>
<body>
    <h1>ovladani LED</h1>
    <p><a href="/?led=on">Zapnout</a></p>
    <p><a href="/?led=off">Vypnout</a></p>
    <p>{led_state}</p>
</body>
</html>
"""
    cl.send(response)
    cl.close()
