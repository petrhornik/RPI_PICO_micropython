from time import sleep
from machine import Pin,PWM

led = PWM(Pin(13))	#PWM=modulace signálu. Určujeme jaký pin bude vysílat modulovaný signál. Intenzita závicí na mezeře mezi signály.
led.freq(1000)	#frekvence která bude aplikována
kroky = 1	#počet proků za sekundu. Čím více kroků tím rychlejší. 


while True:
      for cyklus_kroku in range(0, 65536, kroky):	# (1. číslo, konečné číslo, počet kroků mezi čísly) 
        led.duty_u16(cyklus_kroku)					#.duty = jak dlouho je signál během jednoho cyklu zapnutý(1) ve srovnání s tím, jak dlouho je vypnutý(0)
        #sleep(0.005)               				# čím déle bude signál setrvávat ve vyšší pozici(1)a méně v nižší(0) tak intenzita světla bude vyšší(lze např.: reguluvat i rychlost el. motoru)
                                                    # u16 znamená 16b číslo(max.65536(2^16) = 100% světla)
    
      for cyklus_kroku in range(65536, 0, -kroky):
        led.duty_u16(cyklus_kroku)
        #sleep(0.005)