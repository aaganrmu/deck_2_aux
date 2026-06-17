# deck_2_aux
Circuitpython code for deck 2 auxiliary controler. Uses rp2040-zero.


# Hardware and ports

## SH1106 screen
Colour  Screen  rp2040
White   VCC     +5v
Grey    Gnd     Gnd
Purple  SCK     GP1 (I2C0)
Blue    SDA     GP0 (I2C0)

## Push button
Colour  RP2040
Red     13
Brown   28

## Selector
Switch  rp2040
Top     14
Mid1    15
Mid2    26
Bot     27
Common  28

# Making images
Gimp:
Image -> Mode -> Indexed -> Use black and white (1-bit_ palette)
Export
16 bit (R5G6B5)