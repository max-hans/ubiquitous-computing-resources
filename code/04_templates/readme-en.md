# Block 4: Templates

Starting points for your own prototypes. Each template demonstrates a concrete behaviour — the named variables at the top of the file are meant to be tweaked.

Copy `library.py` from the root `code/` folder to the Pico alongside the template file.

## Templates

| File | Behaviour | Inspiration |
|---|---|---|
| `01_button-trigger.py` | Servo snaps back and forth while button is held | Startled reaction, flinching |
| `02_light-seek.py` | Servo slowly moves toward a target when light is detected, retreats when dark | Plant turning toward the sun |
| `03_two-servos-light.py` | Two servos move in opposite directions based on light | Opening/closing, breathing, an iris |
| `04_nervous.py` | Servo trembles in the dark, calms down in light | Nervousness, anxiety, alertness |

## Notes

- Calibrate `THRESHOLD` using `01_light-sensor.py` from Block 3 first.
- `SPEED` and `AMPLITUDE` control how pronounced the behaviour feels.
- Templates can be combined — e.g. button triggers nervous trembling, light calms it down.
