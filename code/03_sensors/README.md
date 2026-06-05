# Block 3: Sensoren

Sensoren auslesen und mit Outputs verknüpfen.

## Voraussetzungen

- Raspberry Pi Pico
- `library.py` und `paj7620.py` aus dem Hauptordner (`code/`) zusammen mit der Beispieldatei auf den Pico kopieren
- Lichtsensor (analog) an Pin 28
- Taster an Pin 15 (mit Pull-Down)
- Servo an Pin 27

## Beispiele

| Datei                  | Thema                                 |
| ---------------------- | ------------------------------------- |
| `01_light-sensor.py`   | Lichtsensor auslesen (ADC)            |
| `02_button.py`         | Taster auslesen und Wert ausgeben     |
| `03_button-led.py`     | Taster gedrückt → LED an              |
| `04_light-servo.py`    | Lichtwert steuert Servowinkel         |
| `05_gesture-sensor.py` | Geste erkennen und ausgeben (PAJ7620) |

## Aufgaben

1. Finde in `01_light-sensor.py` einen Schwellenwert der „hell" von „dunkel" trennt.
2. Erweitere `02_button.py`: zähle wie oft der Taster gedrückt wurde und gib den Zählerstand aus.
3. Ändere `03_button-led.py` so, dass die LED beim Drücken toggelt statt nur zu leuchten solange gedrückt.
4. Ändere `04_light-servo.py` so, dass der Servo nur zwei Positionen kennt: hell → 0°, dunkel → 180°.
5. Lass in `05_gesture-sensor.py` nur eine bestimmte Geste reagieren – ignoriere alle anderen.
