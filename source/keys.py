import board
import digitalio
import keypad

KEYBINDS = ["up", "down", "enter", "back"]

class Press():
    def __init__(self, key, pressed=True):
        self.key = KEYBINDS[key]
        self.pressed = pressed


class Keys():
    def __init__(self):
        self._keys = keypad.Keys(
        [getattr(board, f'GP{pin}') for pin in [18,19,20,21]],
        value_when_pressed=False,
        pull=True,
        max_events=10
       )
    
    def get_event(self):
        event = self._keys.events.get()
        if event:
            return Press(event.key_number, event.pressed)