# Block 3: Sensoren

Sensoren auslesen und mit Outputs verknüpfen.

## Voraussetzungen

- Raspberry Pi Pico
- `library.py` aus dem Hauptordner (`code/`) zusammen mit der Beispieldatei auf den Pico kopieren
- Lichtsensor (analog) an Pin 28
- Taster an Pin 15 (mit Pull-Down)
- Servo an Pin 27

## Beispiele

| Datei | Thema |
|---|---|
| `01_light-sensor.py` | Lichtsensor auslesen (ADC) |
| `02_button.py` | Taster auslesen und Wert ausgeben |
| `03_button-led.py` | Taster gedrückt → LED an |
| `04_light-servo.py` | Lichtwert steuert Servowinkel |

## Aufgaben

1. Erweitere `01_light-sensor.py`: gib statt des Rohwerts aus, ob es „hell" oder „dunkel" ist – wähle selbst einen sinnvollen Schwellenwert.
2. Erweitere `02_button.py`: zähle wie oft der Taster gedrückt wurde und gib den Zählerstand aus.
3. Ändere `03_button-led.py` so, dass die LED beim Drücken des Tasters toggelt (einmal drücken = an, nochmal drücken = aus).
4. Ändere `04_light-servo.py` so, dass der Servo nur zwei Positionen kennt: bei hellem Licht `0°`, bei Dunkelheit `180°`.
5. Ersetze in `04_light-servo.py` den Lichtsensor durch den Taster: jeder Druck wechselt den Servo zwischen `0°` und `90°`.
