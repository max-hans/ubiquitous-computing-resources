from machine import Pin
from time import sleep


button = Pin(0, Pin.IN)
led = Pin(25, Pin.OUT)

counter = 0
lastValue = 1
lastLed = 0

while True:
    value = button.value()
    
    if value == 0 and lastValue == 1:
        counter = counter + 1
        if lastLed == 0:
            led.value(1)
            lastLed = 1
        else:
            led.value(0)
            lastLed = 0
    
    lastValue = value
    
    print(counter)
    sleep(0.1)
