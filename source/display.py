import adafruit_displayio_sh1106
import busio
import displayio
import bitmaptools
import terminalio
from i2cdisplaybus import I2CDisplayBus 
from lib.adafruit_display_text import label
from adafruit_binascii import a2b_base64
import adafruit_imageload

from logic import State

# Display layout:
# Total display: 128 x 64
# Left side: 5 x 64, 4 tabs, 16 pixels each
# Main screen: 123 x 64
# 

# Display settings
WIDTH = 128
HEIGHT = 64
MEM_OFFSET = 2

# Display tab settings
TAB_HEIGHT = 16
TAB_WIDTH = 4


# Pre-define pallettes
palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

palette_inv = displayio.Palette(2)
palette_inv[0] = 0xFFFFFF
palette_inv[1] = 0x000000 

tab_active, palette_png = adafruit_imageload.load(
    "images/tab_active.png", bitmap=displayio.Bitmap, palette=displayio.Palette
)

tab_inactive, _ = adafruit_imageload.load(
    "images/tab_inactive.png", bitmap=displayio.Bitmap, palette=displayio.Palette
)

# single pixel:
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)

class Display():
    def __init__(self, clk_pin, sda_pin):
        displayio.release_displays()
        i2c = busio.I2C(clk_pin, sda_pin, frequency=1000000)

        display_bus = I2CDisplayBus(i2c, device_address=0x3C)
        self._display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH+MEM_OFFSET, height=HEIGHT)
        self._main_display_modes = [self.main_mode_0, self.main_mode_1, self.main_mode_2, self.main_mode_3]

    def update_display(self, state: State):
        if state.mode == 0:
            current_palette = palette_inv if state.button else palette
        else:
            current_palette = palette
            
        root = displayio.Group(x=MEM_OFFSET)
        root.append(self.background(current_palette))
        root.append(self.tabs(current_palette, state))
        root.append(self.main_window(current_palette, state))
        self._display.root_group = root


    def background(self, palette: displayio.Palette):
        background = displayio.TileGrid(color_bitmap, pixel_shader=palette, x=0, y=0)
        return background


    def tabs(self, palette: displayio.Palette, state: State):
        tabs = displayio.Group()
        for i in range(0,4):
            if i == state.mode:
                tab = tab_active
            else:
                tab = tab_inactive
            grid = displayio.TileGrid(tab, pixel_shader=palette_png, x=0, y=(TAB_HEIGHT)*i+1)
            tabs.append(grid)
        return tabs
        
    def main_window(self, palette: displayio.Palette, state: State):
        main_window = displayio.Group()
        main_window.append(self._main_display_modes[state.mode](palette, state))
        return main_window
    
    def main_mode_0(self, pallette: displayio.Palette, state: State):
        text = "Mode 0: inverted" if state.button else "Mode 0: normal"
        text_area = label.Label(terminalio.FONT, text=text, color=pallette[1], x=10, y=30)
        return text_area

    def main_mode_1(self, pallette: displayio.Palette, state: State):
        text = "Button pressed" if state.button else "Button released"
        text_area = label.Label(terminalio.FONT, text=text, color=pallette[1], x=10, y=30)
        return text_area

    def main_mode_2(self, pallette: displayio.Palette, state: State):
        text = "Mode 2"
        text_area = label.Label(terminalio.FONT, text=text, color=pallette[1], x=10, y=30)
        return text_area
    
    def main_mode_3(self, pallette: displayio.Palette, state: State):
        text = "Mode 3"
        text_area = label.Label(terminalio.FONT, text=text, color=pallette[1], x=10, y=30)
        return text_area
    