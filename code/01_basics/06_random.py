from random import randrange

from time import sleep

while True:    
    value = randrange(2,10) * 0.1
    sleep(value)    
    print("an")
    value = randrange(2,10) * 0.1
    sleep(value)
    print("aus")
