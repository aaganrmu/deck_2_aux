import board
import time
from display import Display
from controls import Controls
from logic import Logic
import digitalio
import random
import neopixel

# setup default blinking led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

display = Display()
controls = Controls()
logic = Logic()

pixel = neopixel.NeoPixel(board.GP2, 1, brightness=0.2, auto_write=False)

colours = [(0,0,0), (255,0,0), (0,255,0), (0,0,255)]

while True:
    display.update_display(logic.state)
    event = controls.get_event()
    if event:
        logic.handle_event(event)

    colour = colours[logic.state.mode]

    pixel.fill(colour)
    pixel.show()