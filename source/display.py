import adafruit_displayio_sh1106
import displayio
import bitmaptools
import terminalio
import os
from lib.adafruit_display_text import label

# Display sizes
WIDTH = 128
HEIGHT = 64
TAB_HEIGHT = 16
TAB_WIDTH = 4
MEM_OFFSET = 2

# colours
BLACK = 0x000000
WHITE = 0xFFFFFF

# Pre-define pallettes
palette = displayio.Palette(2)
palette[0] = BLACK
palette[1] = WHITE

palette_inv = displayio.Palette(2)
palette_inv[0] = WHITE
palette_inv[1] = BLACK


# Load images
image_files = os.listdir("/images")
images = {}
for image_file in image_files:
    name = image_file[:-4]
    images[name]=displayio.OnDiskBitmap(f"/images/{image_file}")

class Display():
    def __init__(self, i2c):
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
        self._display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH+MEM_OFFSET, height=HEIGHT)

    def update_display(self, state):
        root = displayio.Group(x=MEM_OFFSET)
        root.append(self.tabs(state.mode))
        root.append(self.content(state))
        self._display.root_group = root

    def tabs(self, mode):
        tabs = displayio.Group()
        for i in range(0,4):
            if i == mode:
                tab = images["tab_active"]
            else:
                tab = images["tab_inactive"]
            grid = displayio.TileGrid(tab, pixel_shader=palette, x=0, y=(TAB_HEIGHT)*i+1)
            tabs.append(grid)
        return tabs



    def content(self,state):
        content = displayio.Group()
        if state.mode == 0:
            time = state.time
            time_text = f"{time["hour"]}:{time["minute"]}:{time["second"]}"
            time_rendered = label.Label(terminalio.FONT, text=time_text, color=WHITE)
            time_rendered.x = TAB_WIDTH + 4
            time_rendered.y = int(TAB_HEIGHT / 2)
            content.append(time_rendered)
        return content
