import time
from library import Servo

servo = Servo(pin=28)

while True:
    for angle in range(0, 91, 5):
        servo.move(angle)
        time.sleep(0.01)
    time.sleep(0.5)

    for angle in range(90, -1, -5):
        servo.move(angle)
        time.sleep(0.01)
    time.sleep(0.5)
