# Simple test for NeoPixels on Raspberry Pi
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
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

min = 25
max = 75

while True:
    # Fade in
    for k in range (min, max):
        pixels.fill((k, 0, 0))
        pixels.show()
        time.sleep(.1)
    
    # Fade out
    for k in range (max, min, -1):
        pixels.fill((k, 0, 0))
        pixels.show()
        time.sleep(.1)