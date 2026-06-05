from machine import ADC, Pin
from library import Servo
from time import sleep

adc = ADC(Pin(28, Pin.IN))
servo_a = Servo(pin=27)
servo_b = Servo(pin=26)

THRESHOLD = 30000   # Schwellenwert – anpassen je nach Lichtverhältnis
SPEED = 0.008       # kleiner = schneller

current = 90
servo_a.move(current)
servo_b.move(current)

while True:
    light = adc.read_u16()

    if light > THRESHOLD:
        if current < 160:
            current += 1
    else:
        if current > 20:
            current -= 1

    servo_a.move(current)
    servo_b.move(180 - current)  # gegensätzlich
    sleep(SPEED)
