import board
import digitalio
import time
import random

import busio
import displayio
import terminalio
from lib.adafruit_display_text import label
import adafruit_displayio_sh1106

# setup default blinking led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


displayio.release_displays()

i2c = busio.I2C(board.GP1, board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH+2, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(8, 8, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=8)
splash.append(bg_sprite)

while True:
    for i in range(8, WIDTH-8):
        bg_sprite.x = i
        time.sleep(0.002)