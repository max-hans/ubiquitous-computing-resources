from machine import ADC, Pin
from library import Servo
from time import sleep

adc = ADC(Pin(28, Pin.IN))
servo = Servo(pin=27)

THRESHOLD = 30000   # Schwellenwert – anpassen je nach Lichtverhältnis
TARGET = 150        # Zielposition wenn hell
IDLE = 90           # Ruheposition wenn dunkel
SPEED = 0.005       # kleiner = schneller

current = IDLE
servo.move(current)

while True:
    light = adc.read_u16()

    if light > THRESHOLD:
        if current < TARGET:
            current += 1
            servo.move(current)
    else:
        if current > IDLE:
            current -= 1
            servo.move(current)

    sleep(SPEED)
