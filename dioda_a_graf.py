# blikani diody s grafem :)

from time import sleep
from machine import Pin,PWM
import matplotlib.pyplot as plt

led = PWM(Pin(13))
led.freq(1000)
kroky = 1
dataX= []
dataY= []

while True:
      for cyklus_kroku in range(0, 65536, kroky):
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)          
                                                  
    
      for cyklus_kroku in range(65536, 0, -kroky):
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)


def read_data():
    # Simulace čtení dat z MicroPythonu
    # V reálném případě by se data četla přes sériovou komunikaci
    return int(input("Zadej stav LED (0 nebo 1): "))

# Hlavní smyčka pro sběr dat
start_time = time.time()
while len(dataX) < 10:  # Sbíráme 10 vzorků
    current_time = time.time() - start_time
    led_state = read_data()
    dataX.append(current_time)
    dataY.append(led_state)
    time.sleep(1)

# Vykreslení grafu
plt.plot(dataX, dataY, marker='o')
plt.xlabel('Čas (s)')
plt.ylabel('Stav LED (0 = zhasnuto, 1 = rozsvíceno)')
plt.title('Stav LED diody v reálném čase')
plt.show()
