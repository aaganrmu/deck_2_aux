import neopixel

class RGBLed ():
    def __init__(self, pin):
        self._pixel = neopixel.NeoPixel(pin, 1, brightness=0.2, auto_write=False)
        self._colours = [(255,0,0), (0,255,0), (0,0,255), (0,0,0)]

    def update(self, state):
        colour = self._colours[state.mode]
        self._pixel.fill(colour)
        self._pixel.show()