# Simple test for NeoPixels on Raspberry Pi
import sys
import time
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

# Default brightness level
brightlevel = .2

# Change if there is an argument
try:
    brightin = float(sys.argv[1])
    if (brightin <= 1 and brightin >= 0):
        brightlevel = brightin
except IndexError:
    print("No brightness level given. Default = 0.2")


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=brightlevel, auto_write=False, pixel_order=ORDER
)
 
 
pixels.fill((255, 255, 255))
pixels.show()
