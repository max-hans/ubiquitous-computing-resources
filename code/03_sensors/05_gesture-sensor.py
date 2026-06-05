from machine import I2C, Pin
from paj7620 import PAJ7620
from time import sleep

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=50000)
sensor = PAJ7620(i2c)

while True:
    gesture = sensor.read_gesture()
    if gesture:
        print(gesture)
    sleep(0.05)
