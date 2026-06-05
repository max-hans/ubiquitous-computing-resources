import time
from library import Servo

servo = Servo(pin=28)

while True:
    servo.move(0)
    time.sleep(0.5)
    servo.move(90)
    time.sleep(0.5)
