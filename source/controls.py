import board
import digitalio
import keypad

KEYBINDS = {"up":18, "down":19, "enter":20, "back":21,
 "toggle0":10, "toggle1":11, "toggle2":12, "toggle3":13}

class Press():
    def __init__(self, key, pressed=True):
        self.key = key
        self.pressed = pressed

class Controls():
    def __init__(self):
        self._bindings, self._pins = zip(*KEYBINDS.items())
        self._keys = keypad.Keys(
        [getattr(board, f'GP{pin}') for pin in self._pins],
        value_when_pressed=False,
        pull=True,
        max_events=10
       )
    
    def get_event(self):
        event = self._keys.events.get()
        if event:
            key = self._bindings[event.key_number]
            return Press(key, event.pressed)