import board
import time
from display import Display
from keys import Keys
from logic import Logic
import digitalio
import random
import neopixel

# setup default blinking led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

my_display = Display()
my_keys = Keys()
my_logic = Logic()

pixel = neopixel.NeoPixel(board.GP2, 1, brightness=0.2, auto_write=False)

colours = [(0,0,0), (255,0,0), (0,255,0), (0,0,255)]

while True:
    my_display.update_display(my_logic.state)
    event = my_keys.get_event()
    if event:
        my_logic.handle_event(event)

    colour = colours[my_logic.state.mode]

    pixel.fill(colour)
    pixel.show()