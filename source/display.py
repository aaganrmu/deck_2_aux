import adafruit_displayio_sh1106
import board
import busio
import displayio
import bitmaptools
import terminalio
from lib.adafruit_display_text import label
from adafruit_binascii import a2b_base64 

# Display sizes
WIDTH = 128
HEIGHT = 64
TAB_HEIGHT = 16
TAB_WIDTH = 4
MEM_OFFSET = 2


# Pre-define pallettes
palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

palette_inv = displayio.Palette(2)
palette_inv[0] = 0xFFFFFF
palette_inv[1] = 0x000000 


# Pre-render tabs
tab_active = displayio.Bitmap(TAB_WIDTH, TAB_HEIGHT-2, 2)
bitmaptools.arrayblit(tab_active, a2b_base64(b"AQEBAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQA=\n"))

tab_inactive = displayio.Bitmap(TAB_WIDTH, TAB_HEIGHT-2, 2)
bitmaptools.arrayblit(tab_inactive, a2b_base64(b"AQEBAAAAAQEAAAABAAAAAQAAAAEAAAABAAAAAQAAAAEAAAABAAAAAQAAAAEAAAABAAABAQEBAQA=\n"))


class Display():
    def __init__(self):
        displayio.release_displays()
        i2c = busio.I2C(board.GP1, board.GP0)
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
        self._display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH+MEM_OFFSET, height=HEIGHT)

    def update_display(self, state):
        root = displayio.Group(x=MEM_OFFSET)
        root.append(self.tabs(state.mode))
        self._display.root_group = root

    def tabs(self, mode):
        tabs = displayio.Group()
        for i in range(0,4):
            if i == mode:
                tab = tab_active
            else:
                tab = tab_inactive
            grid = displayio.TileGrid(tab, pixel_shader=palette, x=0, y=(TAB_HEIGHT)*i+1)
            tabs.append(grid)
        return tabs