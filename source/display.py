import adafruit_displayio_sh1106
import displayio
import bitmaptools
import terminalio
from i2cdisplaybus import I2CDisplayBus 
from lib.adafruit_display_text import label
from adafruit_binascii import a2b_base64


from logic import State

# Display layout:
# Total display: 128 x 64
# Left side: 5 x 64, 4 tabs, 16 pixels each
# Main screen: 123 x 64
# 
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


# Pre-render tabs
tab_active = displayio.Bitmap(TAB_WIDTH, TAB_HEIGHT-2, 2)
bitmaptools.arrayblit(tab_active, a2b_base64(b"AQEBAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQA=\n"))

tab_inactive = displayio.Bitmap(TAB_WIDTH, TAB_HEIGHT-2, 2)
bitmaptools.arrayblit(tab_inactive, a2b_base64(b"AQEBAAAAAQEAAAABAAAAAQAAAAEAAAABAAAAAQAAAAEAAAABAAAAAQAAAAEAAAABAAABAQEBAQA=\n"))

# single pixel:
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)

class Display():
    def __init__(self, i2c:I2CDisplayBus):
        display_bus = I2CDisplayBus(i2c, device_address=0x3C)
        self._display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH+MEM_OFFSET, height=HEIGHT)


    def update_display(self, state: State):
        current_palette = palette_inv if state.button else palette
       
        root = displayio.Group(x=MEM_OFFSET)
        root.append(self.background(current_palette))
        root.append(self.tabs(current_palette, state.mode))
        self._display.root_group = root


    def background(self, palette: displayio.Palette):
        background = displayio.TileGrid(color_bitmap, pixel_shader=palette, x=0, y=0)
        return background


    def tabs(self, palette: displayio.Palette, mode: int):
        tabs = displayio.Group()
        for i in range(0,4):
            if i == mode:
                tab = tab_active
            else:
                tab = tab_inactive
            grid = displayio.TileGrid(tab, pixel_shader=palette, x=0, y=(TAB_HEIGHT)*i+1)
            tabs.append(grid)
        return tabs