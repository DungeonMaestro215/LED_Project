# Simple test for NeoPixels on Raspberry Pi
import sys
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
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


width = 10
color = (150, 0, 150)
# Change if there is an argument
try:
    widthin = int(sys.argv[1])
    if (widthin <= 300 and widthin > 0):
        width = widthin
except IndexError:
    print("Using default width.")    

# number for width

bitch = range(-1 * width, 0)

n = 0 #pixel index

while (True):

    # time.sleep could go here
    time.sleep(.001)

    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    for daphne in bitch:
        pixels[n + daphne] = color

    if n == num_pixels - 1:
        n = 0  # if it go to the end, go back to the start
    else:
        n = n + 1 #gg go next

    pixels.show()
