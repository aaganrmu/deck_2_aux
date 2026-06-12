import board
import busio
from display import Display
from controls import Controls
from logic import Logic
import neopixel
import displayio
import digitalio   

displayio.release_displays()
pin_clk = board.GP1
pin_sda = board.GP0
try:
    i2c = busio.I2C(pin_clk, pin_sda)
except TimeoutError as e:
    print(f"Error initializing I2C: {e}")

# display = Display(i2c)
controls = Controls()
logic = Logic()

pin_common = digitalio.DigitalInOut(board.GP28)
pin_common.direction = digitalio.Direction.OUTPUT
pin_common.value = True
                       


pixel = neopixel.NeoPixel(board.GP16, 1, brightness=0.2, auto_write=False)

colours = [(0,0,0), (255,0,0), (0,255,0), (0,0,255)]

while True:
    # display.update_display(logic.state)
    event = controls.get_event()
    if event:
        logic.handle_event(event)

    colour = colours[logic.state.mode]

    pixel.fill(colour)
    pixel.show()