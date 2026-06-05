from machine import Pin
from library import Servo
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
servo = Servo(pin=28)

POSITION_IDLE = 90
POSITION_A = 20
POSITION_B = 160
SPEED = 0.01  # kleiner = schneller

servo.move(POSITION_IDLE)

while True:
    if button.value() == 1:
        servo.move(POSITION_A)
        sleep(SPEED)
        servo.move(POSITION_B)
        sleep(SPEED)
    else:
        servo.move(POSITION_IDLE)
    sleep(0.01)
