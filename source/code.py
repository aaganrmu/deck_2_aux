import board

from controls import Controls
from display import Display
from logic import Logic
from rgbled import RGBLed


DISPLAY_PINS = { # Pins for the I2C display
    "CLK": board.GP1,
    "SDA": board.GP0,
}

HIGH_PIN = board.GP28 # Common pins of the switches
KEYBINDS = { # Pins for one push button and a 4 way rotary switch
    "button0":13, 
    "toggle0":14,
    "toggle1":15,
    "toggle2":26,
    "toggle3":27,
    }

PIXEL_PIN = board.GP16 # A single neopixel

# Initialize all components
controls = Controls(KEYBINDS, HIGH_PIN)
display = Display(DISPLAY_PINS["CLK"], DISPLAY_PINS["SDA"])
logic = Logic()
rgbled = RGBLed(PIXEL_PIN)


while True:    
    display.update_display(logic.state)
    rgbled.update(logic.state)
    
    while (event := controls.get_event()):
        logic.handle_event(event)
