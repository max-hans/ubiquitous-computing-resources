from machine import Pin
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

while True:
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)
    sleep(0.05)
