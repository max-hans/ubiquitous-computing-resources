# Block 2: Outputs

Erste Schritte mit dem Pico – LEDs und Servos ansteuern.

## Voraussetzungen

- Raspberry Pi Pico
- `library.py` aus dem Hauptordner (`code/`) zusammen mit der Beispieldatei auf den Pico kopieren
- Für Servos: SG90 an Pin 28 (und Pin 27 für den zweiten Servo)

## Beispiele

| Datei               | Thema                                     |
| ------------------- | ----------------------------------------- |
| `01_led.py`         | Onboard-LED blinken lassen                |
| `02_blink.py`       | LED mit nicht-blockierendem Blinky-Objekt |
| `03_servo.py`       | Servo zwischen 0° und 90° wechseln        |
| `04_servo-fade.py`  | Servo sanft von 0° auf 90° fahren         |
| `05_multi-servo.py` | Zwei Servos gleichzeitig steuern          |

## Aufgaben

1. Lass die LED in `01_led.py` deutlich schneller blinken.
2. Lass den Servo in `03_servo.py` den vollen Bewegungsbereich ausnutzen.
3. Lass den Servo in `04_servo-fade.py` so langsam fahren, dass die Bewegung kaum wahrnehmbar ist.
4. Lass die beiden Servos in `05_multi-servo.py` in entgegengesetzte Richtungen fahren.
5. Kombiniere LED und Servo: die LED soll nur leuchten, wenn der Servo bei `90°` steht.
