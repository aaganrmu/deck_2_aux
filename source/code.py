import board
import busio
import time
from display import Display
from controls import Controls
from logic import Logic
from clockie import Clockie
import digitalio
import random
import neopixel
import displayio


# setup default blinking led
# led = digitalio.DigitalInOut(board.LED)
# led.direction = digitalio.Direction.OUTPUT


displayio.release_displays()
i2c = busio.I2C(board.GP1, board.GP0)

display = Display(i2c)
controls = Controls()
logic = Logic()
logic.set_clock(Clockie(i2c))

 
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