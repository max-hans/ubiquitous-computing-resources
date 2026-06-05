from math import sin
from time import time, sleep

while True:
    value = (sin(time()) + 1) / 2
    print(value)
    sleep(0.1)
