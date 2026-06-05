# "Ubiquitous Computing" Course Material

Maximilian Hans, HfG Karlsruhe

Contact: main@i-like-robots.com

![](resources/header.png)

## Resources

- <a href="https://raw.githubusercontent.com/max-hans/25-hfg-karlsruhe-arduino/refs/heads/main/resources/1-intro.pdf" class="image fit">01-intro</a>
- <a href="https://raw.githubusercontent.com/max-hans/25-hfg-karlsruhe-arduino/refs/heads/main/resources/2-inspiration.pdf" class="image fit">02-inspiration</a>
- <a href="https://github.com/max-hans/25-hfg-karlsruhe-arduino/archive/refs/heads/main.zip">Download all files</a>
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

## Prompting

When using ChatGPT or other GenAi to work on your code, integrate the following in your prompt:

```
<context>
we are using microphyton on a pi pico. make the code as simple as possible.
dont use any fancy python functionality. dont use defs/functions, consts, type annotations, records or array.
dont rewrite the code from ground up.
use only the libraries: "time" and "machine".
the code should be verbose without making things too complex. dont add extraneous comments. the code should explain itself.
if something is unclear (pins, timeframes etc) – ask before creating the code.

The pi pico has 28 GPIO pins going from GP0 to GP28. GP23-GP25 are NOT available.
GP26, GP27 and GP28 can also be used as ADC.
</context>
```

### Example prompt

---

```
<context>
we are using microphyton on a pi pico. make the code as simple as possible.
dont use any fancy python functionality. dont use defs/functions, consts, type annotations, records or array.
dont rewrite the code from ground up.
use only the libraries: "time" and "machine".
the code should be verbose without making things too complex. dont add extraneous comments. the code should explain itself.
if something is unclear (pins, timeframes etc) – ask before creating the code.
</context>
```

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

---
