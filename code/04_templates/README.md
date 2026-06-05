# Block 4: Templates

Startpunkte für eigene Prototypen. Jedes Template zeigt ein konkretes Verhalten – die markierten Variablen oben im Code sind zum Anpassen gedacht.

`library.py` aus dem Hauptordner (`code/`) zusammen mit der Template-Datei auf den Pico kopieren.

## Templates

| Datei | Verhalten | Inspiration |
|---|---|---|
| `01_button-trigger.py` | Servo bewegt sich schnell hin und her, solange der Taster gedrückt ist | Erschrecken, Abwehr, Reaktion |
| `02_light-seek.py` | Servo fährt langsam zu einer Zielposition, wenn Licht erkannt wird – zieht sich zurück wenn dunkel | Pflanze die sich zur Sonne dreht |
| `03_two-servos-light.py` | Zwei Servos bewegen sich gegensätzlich je nach Licht | Öffnen / Schließen, Atmen, Blende |
| `04_nervous.py` | Servo zittert im Dunkeln, beruhigt sich im Hellen | Nervosität, Angst, Aufmerksamkeit |

## Hinweise

- `THRESHOLD` bestimmt ab welchem Lichtwert das Verhalten wechselt – erst mit `01_light-sensor.py` aus Block 3 kalibrieren.
- `SPEED` und `AMPLITUDE` steuern wie ausgeprägt das Verhalten wirkt.
- Templates kombinieren: z.B. Button triggert nervöses Zittern, Licht beruhigt.
