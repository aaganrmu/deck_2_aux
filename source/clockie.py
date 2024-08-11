
import adafruit_ds3231


class Clockie():
    def __init__(self, i2c):
        self._rtc = adafruit_ds3231.DS3231(i2c)

    @property
    def time(self):
        t = self._rtc.datetime
        time_object = {"hour":t.tm_hour, "minute": t.tm_min, "second": t.tm_sec}
        return time_object

    @time.setter
    def time(self, time):
        pass
        # [TODO] implement RTC time updater