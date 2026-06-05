from machine import ADC, Pin
from library import Servo
from utime import ticks_ms, sleep_ms
from math import sin

adc = ADC(Pin(28, Pin.IN))
servo = Servo(pin=28)

THRESHOLD = 25000   # unter diesem Wert: nervös
CENTER = 90         # Ruheposition
AMPLITUDE = 12      # Ausschlag in Grad – größer = nervöser
FREQUENCY = 0.025   # größer = schneller

while True:
    light = adc.read_u16()

    if light < THRESHOLD:
        offset = sin(ticks_ms() * FREQUENCY) * AMPLITUDE
        servo.move(CENTER + offset)
    else:
        servo.move(CENTER)

    sleep_ms(20)
