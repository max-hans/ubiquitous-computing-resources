import time

DEFAULT_ADDR = 0x73

REG_BANK_SEL = 0xEF
REG_CHIP_ID_L = 0x00
REG_CHIP_ID_H = 0x01
REG_GESTURE_FLAG = 0x43
REG_GESTURE_DATA = 0x44

GESTURES = {
    0x01: "UP",
    0x02: "DOWN",
    0x04: "LEFT",
    0x08: "RIGHT",
    0x10: "FORWARD",
    0x20: "BACKWARD",
    0x40: "CLOCKWISE",
    0x80: "ANTICLOCKWISE",
}

INIT_REGISTERS = [
    (0xEF, 0x00),
    (0x32, 0x29),
    (0x33, 0x01),
    (0x34, 0x00),
    (0x35, 0x01),
    (0x36, 0x00),
    (0x37, 0x07),
    (0x38, 0x17),
    (0x39, 0x06),
    (0x3A, 0x12),
    (0x3F, 0x00),
    (0x40, 0x02),
    (0x41, 0xFF),
    (0x42, 0x01),
    (0x46, 0x2D),
    (0x47, 0x0F),
    (0x48, 0x3C),
    (0x49, 0x00),
    (0x4A, 0x1E),
    (0x4B, 0x00),
    (0x4C, 0x20),
    (0x4D, 0x00),
    (0x4E, 0x1A),
    (0x4F, 0x14),
    (0x50, 0x00),
    (0x51, 0x10),
    (0x52, 0x00),
    (0xEF, 0x01),
    (0x00, 0x1E),
    (0x01, 0x1E),
    (0x02, 0x0F),
    (0x03, 0x10),
    (0x04, 0x02),
    (0x05, 0x00),
    (0x06, 0xB0),
    (0x07, 0x04),
    (0x08, 0x0D),
    (0x09, 0x0E),
    (0x0A, 0x9C),
    (0x0B, 0x04),
    (0x0C, 0x05),
    (0x0D, 0x0F),
    (0x0E, 0x02),
    (0x0F, 0x12),
    (0x10, 0x02),
    (0x11, 0x02),
    (0x12, 0x00),
    (0x13, 0x01),
    (0xEF, 0x00),
]


class PAJ7620:
    def __init__(self, i2c, address=DEFAULT_ADDR, debug=False):
        self.i2c = i2c
        self.address = address
        self.debug = debug
        self._init_sensor()

    def _write(self, reg, val):
        self.i2c.writeto(self.address, bytes([reg, val]))

    def _read(self, reg):
        self.i2c.writeto(self.address, bytes([reg]))
        return self.i2c.readfrom(self.address, 1)[0]

    def _init_sensor(self):
        self._write(REG_BANK_SEL, 0x00)
        time.sleep_ms(10)

        if self.debug:
            cid_l = self._read(REG_CHIP_ID_L)
            cid_h = self._read(REG_CHIP_ID_H)
            print("PAJ7620 Chip ID:", hex((cid_h << 8) | cid_l))

        for reg, val in INIT_REGISTERS:
            self._write(reg, val)

        self._enable_gesture_mode()

        if self.debug:
            print("PAJ7620 init done")

    def _enable_gesture_mode(self):
        self._write(REG_BANK_SEL, 0x01)
        time.sleep_ms(5)
        self._write(0x72, 0x01)
        self._write(0x73, 0x35)
        self._write(0x74, 0x00)
        self._write(0x75, 0x33)
        self._write(0x76, 0x31)
        self._write(0x77, 0x01)
        self._write(REG_BANK_SEL, 0x00)
        time.sleep_ms(5)

    def read_gesture(self):
        self.i2c.writeto(self.address, bytes([REG_GESTURE_FLAG]))
        buf = self.i2c.readfrom(self.address, 2)
        flag, data = buf[0], buf[1]
        if self.debug:
            print("RAW -> flag:", hex(flag), "data:", hex(data))
        return GESTURES.get(flag)
