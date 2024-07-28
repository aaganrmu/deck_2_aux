import board
import busio
import adafruit_ds3231


class Rtc():
    def __init__(self):
        i2c = board.I2C(board.GP1, board.GP0)
        rtc = adafruit_ds3231.DS3231(i2c)

