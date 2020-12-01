### Set up NeoPixel library and initiate pixel array ###
import sys
import time
import board
import neopixel
import numpy as np

# Choose an open pin connected to the Data In of the NeoPixel strip
pixel_pin = board.D12

# The number of pixels
num_pixels = 300

# The order of the pixel colors 
ORDER = neopixel.GRB

# Set up the array for the strip
pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
        )

# How many arguments will each effect have?
# brightness, beginning, ending, plus 3 extra
num_params = 6

### Get inputs for each effect ###
#effects = float(sys.argv[::num_params])
#params = []


### Master Loop ###
while True:
    for effect in sys.argv[::num_params]:
        print(effect)
