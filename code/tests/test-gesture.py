from machine import SoftI2C, Pin
from paj7620 import PAJ7620
import time

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=50000)

time.sleep_ms(700)
sensor = PAJ7620(i2c)

val = map(1,0,1,0,255)
print(val)

while True:
    g = sensor.read_gesture()
    # print(g)
    if g:
        print("Gesture:", g)
    time.sleep_ms(20)

    # time.sleep(0.05)