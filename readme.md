# "Ubiquitous Computing" Course Material

Maximilian Hans, HfG Karlsruhe

Contact: main@i-like-robots.com

![](resources/header.png)

## Resources

- [Download all files](https://github.com/max-hans/ubiquitous-computing-resources/archive/refs/heads/main.zip)
- [MicroPython Reference](https://docs.micropython.org/en/latest/rp2/quickref.html)

## Introduction

### Thonny

You will need Thonny to run and upload your Python code. Get it [here](https://thonny.org/).

![](resources/thonny.png)

### Getting All the Data

**1. Download the Contents of This Repository**

Click on 'Download .ZIP'

![alt text](resources/github.png)

## Python Basics

You can find a list of examples and descriptions on how Python code actually works [here](/python.md)

## Code Examples

Code examples can be found in the [`code/`](/code) directory, organised in four blocks.

### Block 1 – Python Basics [`code/01_basics`](/code/01_basics)

Pure Python, no microcontroller needed. Covers variables, conditions, loops and signals. Run directly on your computer.

### Block 2 – Outputs [`code/02_outputs`](/code/02_outputs)

Controlling LEDs and servo motors on the Pico.

### Block 3 – Sensors [`code/03_sensors`](/code/03_sensors)

Reading inputs: light sensor, push button, gesture sensor. Includes examples that combine sensors with outputs.

### Block 4 – Templates [`code/04_templates`](/code/04_templates)

Ready-to-run starting points for prototypes. Tweak the parameters at the top of each file to shape the behaviour.

### library.py

Shared code used by Blocks 2–4. Copy it to the Pico alongside whichever example you are running. Do not modify.

## Wiring

### Pinout Pi Pico

![](/resources/pico-pinout.svg)

**⚠️ Make sure the Pi Pico is placed on the breadboard like below ⚠️**

![](resources/breadboard.png)

### Single Servo

![](resources/single-servo.png)

### Multiple Servos

![](resources/multi-servo.png)

### Ultrasonic Sensor

![](resources/ultrasonic.png)

### Light Sensor

![](resources/sensor.png)

## Using AI

You can use AI for your free work. Either copy the system prompt from [here](prompting/system-prompt.md) or use the [Gemini Gem](https://gemini.google.com/gem/1tQuCdHKf2PpdJEWrHFLv_pLEOZo6zHIc?usp=sharing) I created for you to use.

### Example prompt

---

<<< enter the system prompt here or omit when using the Gemini Gem >>>

add a second led, if the value is 1 the first one should light up, if not the second led should light up.

current code:

```
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
sensor = Pin(15,Pin.IN)

while True:

    value = sensor.value()
    print(value)
    if value == 1:
        led.value(1)
    else:
        led.value(0)
    sleep(0.1)

```

## Shops

You can buy electronics components from various sources. Amazon has a pretty broad offering, however products sold there usually lack documentation
and examples.

The shops below usually provide better guidance on what to buy and usually are more approachable.

[https://www.berrybase.de/](berrybase.de)

[https://www.az-delivery.de](az-delivery.de)

[https://www.roboter-bausatz.de](roboter-bausatz.de)

[https://www.conrad.de](conrad.de)
