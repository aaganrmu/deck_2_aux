import board
import digitalio
import keypad

KEYBINDS = {
    "button0":13, 
    "toggle0":14,
    "toggle1":15,
    "toggle2":26,
    "toggle3":27,
    }

class Press():
    def __init__(self, key, pressed=True):
        self.key = key
        self.pressed = pressed

class Controls():
    def __init__(self):
        self._bindings, self._pins = zip(*KEYBINDS.items())
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