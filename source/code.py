import board
import time
from display import Display
from keys import Keys
from logic import Logic
import digitalio

# setup default blinking led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

my_display = Display()
my_keys = Keys()
my_logic = Logic()

while True:
    my_display.update_display(my_logic.state)
    event = my_keys.get_event()
    if event:
        my_logic.handle_event(event)
