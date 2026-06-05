from machine import Pin
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    val = button.value()
    print(val)
    sleep(0.1)
