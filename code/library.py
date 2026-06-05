from machine import Pin, time_pulse_us, PWM
from utime import sleep_us, ticks_ms, ticks_diff
from math import sin, pi


def map_range(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Servo:
    _SERVO_PWM_FREQ = 50
    _MIN_U16_DUTY = 1638
    _MAX_U16_DUTY = 7864

    def __init__(self, pin, min_angle=0, max_angle=180):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = None
        self._angle_conversion_factor = (self._MAX_U16_DUTY - self._MIN_U16_DUTY) / (max_angle - min_angle)
        self._motor = PWM(Pin(pin))
        self._motor.freq(self._SERVO_PWM_FREQ)

    def move(self, angle):
        if angle < self.min_angle or angle > self.max_angle:
            raise ValueError(f"Angle must be between {self.min_angle} and {self.max_angle}")

        angle = round(angle, 2)

        if angle == self.current_angle:
            return

        self.current_angle = angle
        duty_u16 = int((angle - self.min_angle) * self._angle_conversion_factor) + self._MIN_U16_DUTY
        self._motor.duty_u16(duty_u16)


class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        sleep_us(5)
        self.trigger.value(1)
        sleep_us(10)
        self.trigger.value(0)

        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            if pulse_time < 0:
                raise OSError('Out of range')
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        return (self._send_pulse_and_wait() / 2) / 0.0291

    def distance_cm(self):
        return self.distance_mm() / 10


class Blinky:
    def __init__(self, pin):
        if isinstance(pin, int):
            self.pin = Pin(pin, Pin.OUT)
        else:
            self.pin = pin
            self.pin.init(Pin.OUT)

        self.interval = 0
        self.last_update = 0
        self.state = False
        self.running = False

    def start(self, interval):
        self.interval = interval
        self.last_update = ticks_ms()
        self.state = False
        self.pin.value(0)
        self.running = True

    def stop(self):
        self.running = False
        self.pin.value(0)

    def change_frequency(self, new_interval):
        self.interval = new_interval

    def update(self):
        if self.running:
            current_time = ticks_ms()
            if ticks_diff(current_time, self.last_update) >= self.interval:
                self.state = not self.state
                self.pin.value(self.state)
                self.last_update = current_time


class SineGenerator:
    def __init__(self, period=1000):
        self.period = period
        self._running = False
        self._start_time = 0
        self._paused_at = 0

    def start(self):
        self._start_time = ticks_ms()
        self._running = True

    def pause(self):
        if self._running:
            self._paused_at = ticks_diff(ticks_ms(), self._start_time)
            self._running = False

    def resume(self):
        if not self._running:
            self._start_time = ticks_ms() - self._paused_at
            self._running = True

    def update(self):
        if not self._running:
            return None
        elapsed = ticks_diff(ticks_ms(), self._start_time)
        t = (elapsed / self.period) * 2 * pi
        return (sin(t) + 1) / 2  # 0.0 – 1.0