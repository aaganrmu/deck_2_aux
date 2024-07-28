
import adafruit_ds3231


class Clockie():
    def __init__(self, i2c):
        rtc = adafruit_ds3231.DS3231(i2c)

