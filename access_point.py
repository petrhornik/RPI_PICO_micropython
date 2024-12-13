import network
import socket
import time
from machine import Pin

# Vytvoření pinu pro LED (indikace stavu AP)
led = Pin("LED", Pin.OUT)

# Funkce pro inicializaci Wi-Fi jako Access Point
def init_ap():
    ap = network.WLAN(network.AP_IF)  # Vytvoříme objekt pro Access Point
    ap.active(True)  # Aktivujeme Access Point
    ap.config(essid="Pico1234", password="1236456789")  # Nastavení SSID a hesla
    print("Access Point started")
    print("IP address:", ap.ifconfig()[0])  # Získání IP adresy Access Pointu

# HTML stránka, která bude zobrazena po připojení
def webpage():
    html = """<!DOCTYPE html>
<html>
    <head>
        <title>Pico Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>Vítejte na Raspberry Pi Pico W!</h1>
        <p>Gratulujeme! Připojili jste se k Access Pointu Raspberry Pi Pico W.</p>
    </body>
</html>"""
    return html

# Funkce pro obsluhu HTTP požadavků
def handle_request():
    # Vytvoření socketu pro server
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]  # Nasloucháme na portu 80
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print("Server naslouchá na adrese", addr)

    while True:
        # Připojení klienta
        cl, addr = s.accept()
        print('Připojení od:', addr)

        # Čtení požadavku
        request = cl.recv(1024)
        print('Požadavek:', request)

        # Odeslání HTML odpovědi
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: text/html; charset=utf-8\r\n\r\n')
        cl.send(webpage())  # Odeslání HTML obsahu

        cl.close()  # Uzavření spojení

# Hlavní funkce pro spuštění Access Pointu a webového serveru
def main():
    init_ap()  # Inicializace Access Pointu
    handle_request()  # Spuštění serveru pro obsluhu požadavků

# Spuštění hlavní funkce
main()
