
from controls import Press


class State():
    def __init__(self):
        self._mode = 0

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode %4

    @property
    def time(self):
        return self._clock.time

    @time.setter
    def time(self, time):
        self._clock.time = time


class Logic():
    def __init__(self):
        self._state = State()

    def handle_event(self, press):
        if not press.pressed:
            return
        state = self._state
        if press.key == "up":
            state.mode -= 1
        if press.key == "down":
            state.mode += 1
        if "toggle" in press.key:
            state.mode = int(press.key[6:])

    def set_clock(self, clock):
        self._state._clock = clock

    @property
    def state(self):

        return self._state