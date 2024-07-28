import board
import busio
import time
from display import Display
from controls import Controls
from logic import Logic
from clockie import Clockie
import digitalio
import random
import displayio



displayio.release_displays()
i2c = busio.I2C(board.GP1, board.GP0)

display = Display(i2c)
controls = Controls()
logic = Logic()
clockie = Clockie(i2c)

 

while True:
    display.update_display(logic.state)
    event = controls.get_event()
    if event:
        logic.handle_event(event)

    pixel.show()
    clockie.print_time()