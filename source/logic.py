
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

class Logic():
    def __init__(self):
        self._state = State()

    def handle_event(self, press):
        if not press.pressed:
            return false
        state = self._state
        if press.key == "up":
            state.mode -= 1
        if press.key == "down":
            state.mode += 1
        if "toggle" in press.key:
            state.mode = int(press.key[6:])
        return true

    @property
    def state(self):
        return self._state