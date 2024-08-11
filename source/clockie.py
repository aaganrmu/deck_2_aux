
import adafruit_ds3231


class Clockie():
    def __init__(self, i2c):
        self._rtc = adafruit_ds3231.DS3231(i2c)

    def print_time(self):
        t = self._rtc.datetime
        print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')
