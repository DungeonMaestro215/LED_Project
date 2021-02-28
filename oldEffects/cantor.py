# Simple test for NeoPixels on Raspberry Pi
import time
import numpy as np
import board
import neopixel
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12
 
# The number of NeoPixels
num_pixels = 300
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

# Middle 3rd Cantor Set
start = 29
end = 272

top_level = np.rint(np.log(end - start)/np.log(3))
level = top_level

on_color = (0,255,0)
off_color = (0,0,0)

pixels.fill(on_color)

while True:
    # Length of level intervals
    interval = 3**level

    # Does this index belong in this level?
    for idx in range(0, end - start:
        if (idx / interval % 3 >= 1 and idx / interval % 3 < 2):
            pixels[idx + start] = off_color

    # Display
    pixels.show()
    
    # Go down a level, or go back to the top
    if (level == 0):
        level = top_level
    else:
        level -= 1
    time.sleep(1)
