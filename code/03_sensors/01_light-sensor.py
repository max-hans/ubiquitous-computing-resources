from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(28, Pin.IN))

while True:
    value = adc.read_u16()
    print("Lichtwert:", value)
    sleep(0.3)
