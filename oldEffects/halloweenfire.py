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
    pixel_pin, num_pixels, brightness=0.4, auto_write=False, pixel_order=ORDER
)

# Code adapted from:
# https://github.com/danesparza/Halloweenfire/blob/master/halloweenfire.ino

# Flame colors
    # orange, purple, green, red
flame_colors = [ (226, 121, 35), (158, 8, 148), (74, 150, 12), (226, 15, 30)]

num_colors = len(flame_colors)

current_color_idx = 1

ok_to_change_colors = True

pixels.fill((0, 0, 0))
pixels.show()

while True:
    current_color = flame_colors[current_color_idx]
    
    for i in range(len(pixels)):
        flicker = np.random.randint(0, 75)
        r1 = current_color[0] - flicker
        g1 = current_color[1] - flicker
        b1 = current_color[2] - flicker

        r1 = r1 if r1 > 0 else 0
        g1 = g1 if g1 > 0 else 0
        b1 = b1 if b1 > 0 else 0
        
        pixels[i] = (r1, g1, b1)

    pixels.show()
    time.sleep(np.random.randint(10, 113) / 1000)
