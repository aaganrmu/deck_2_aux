from controls import Press

class State():
    def __init__(self):
        self._mode = 0
        self._button = False

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, mode: int):
        self._mode = mode %4

    @property
    def button(self):
        return self._button    
    @button.setter
    def button(self, button: bool):
        self._button = button


class Logic():
    def __init__(self):
        self._state = State()

    def handle_event(self, press: Press):
        state = self._state
        if press.key == "button0":
            state.button = press.pressed

        if not press.pressed:
            return
        if "toggle" in press.key:
            state.mode = int(press.key[6:])
    
    @property
    def state(self):
        return self._state