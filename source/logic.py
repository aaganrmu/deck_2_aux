
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
        state = self._state
        if press.key == "button0":
            if press.pressed:
                print("button0 pressed")
            else:
                print("button0 released")

        if not press.pressed:
            return
        if "toggle" in press.key:
            state.mode = int(press.key[6:])
            print(state.mode)
    @property
    def state(self):
        return self._state