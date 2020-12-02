### Import necessary packages ### 
import sys
import time
import board
import neopixel
import numpy as np

### Import effects and create effect dictionary ###
effect_dict = {}


### Set up NeoPixel pixel array ###
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


### Master Loop ###
try:
    while True:
        # Parse through input
        i = 1
        while (i < len(sys.argv)):
            # Gather necessary information about the effect
            # name of effect, beginning and ending index for effect on the pixel array
            name = sys.argv[i]
            i += 1
            begin, end = map(int, sys.argv[i:i+2])
            i += 2
    
            # Determine the number of extra parameters given for the effect
            j = i
            while (j < len(sys.argv) and sys.argv[j] not in effect_dict):
                j += 1
    
            # Change the appropriate part of the array by running it through the function
            try:
                pixels = pixels[0:begin] + effect_dict[name](pixels[begin:end], *sys.argv[i:j]) + pixels[end:len(pixels)]
            except TypeError:
                print("Error: Too many parameters given for effect '" + name + ".' Check that the correct number of parameters are given and that there are no typos.")
            i = j
        print(pixels)
    
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n\nExiting program...")
