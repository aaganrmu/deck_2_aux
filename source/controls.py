import board
import keypad

class Press():
    def __init__(self, key: str, pressed: bool = True):
        self.key = key
        self.pressed = pressed

class Controls():
    def __init__(self, keybinds: dict[str, int] = {}):
        self._bindings, self._pins = zip(*keybinds.items())
        self._keys = keypad.Keys(
        [getattr(board, f'GP{pin}') for pin in self._pins],
        value_when_pressed=True,
        pull=True,
        max_events=10
       )
    
    def get_event(self):
        event = self._keys.events.get()
        if event:
            key = self._bindings[event.key_number]
            return Press(key, event.pressed)