from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(26, Pin.IN))

total = 0
for i in range(0, 20, 1):
    current_value = adc.read_u16()
    total = total + current_value
    sleep(0.1)
threshold = int(total / 20)


print("Average brightness: " + str(threshold))

while True:
    value = adc.read_u16()
    print("Lichtwert:", value)
    if(value > threshold + 1000):
        print("dunkel")
    else:
        print("hell")
    sleep(0.3)

