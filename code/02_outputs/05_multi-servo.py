import time
from library import Servo

servo1 = Servo(pin=28)
servo2 = Servo(pin=27)

while True:
    servo1.move(0)
    servo2.move(0)
    time.sleep(0.5)
    servo1.move(90)
    servo2.move(90)
    time.sleep(0.5)
