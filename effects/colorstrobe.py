# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import numpy as np
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12
 
# The number of NeoPixels
num_pixels = 300
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=.9, auto_write=False, pixel_order=ORDER
)

wait = .01
while True:
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(.1)
    r = int(np.random.rand() * 255)
    g = int(np.random.rand() * 255)
    b = int(np.random.rand() * 255)
    pixels.fill((r, g, b))
    pixels.show()
    time.sleep(.01)
    
