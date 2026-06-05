from machine import ADC, Pin
from library import Servo
from time import sleep

adc = ADC(Pin(28, Pin.IN))
servo = Servo(pin=27)

while True:
    raw = adc.read_u16()                        # 0 – 65535
    angle = int(raw / 65535 * 180)              # map to 0 – 180°
    print("Lichtwert:", raw, "→ Winkel:", angle)
    servo.move(angle)
    sleep(0.05)
