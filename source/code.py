import board
import busio
from display import Display
from controls import Controls
from logic import Logic
import neopixel
import displayio
import digitalio   


DISPLAY_PINS = {
    "CLK": board.GP1,
    "SDA": board.GP0,
}

KEYBINDS = {
    "button0":13, 
    "toggle0":14,
    "toggle1":15,
    "toggle2":26,
    "toggle3":27,
    }

PIXEL_PIN = board.GP16

HIGH_PIN = board.GP28 # Set to high to drive bound keys

displayio.release_displays()
i2c = busio.I2C(DISPLAY_PINS["CLK"], DISPLAY_PINS["SDA"], frequency=1000000)
display = Display(i2c)

controls = Controls(KEYBINDS)
logic = Logic()

pin_common = digitalio.DigitalInOut(HIGH_PIN)
pin_common.direction = digitalio.Direction.OUTPUT
pin_common.value = True
                       


pixel = neopixel.NeoPixel(PIXEL_PIN, 1, brightness=0.2, auto_write=False)

colours = [(255,0,0), (0,255,0), (0,0,255), (0,0,0)]

while True:
    display.update_display(logic.state)

    event = controls.get_event()
    if event:
        logic.handle_event(event)

    colour = colours[logic.state.mode]

    pixel.fill(colour)
    pixel.show()