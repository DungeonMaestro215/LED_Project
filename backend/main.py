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

# How many arguments will each effect have?
# effect name, brightness, beginning, ending, plus 3 extra is 7
num_params = 7


### Master Loop ###
while True:
    # Every iteration, go through each effect that was given as an argument
    for i in range(1, len(sys.argv), num_params):
        # Gather necessary information about the effect
        name = sys.argv[i]              # Effect name
        bc = float(sys.argv[i + 1])     # Brightness controller for effect (float b/t 0 and 1)
        begin = int(sys.argv[i + 2])    # Starting index for the effect
        end = int(sys.argv[i + 3])      # Ending index for the effct (exclusive)
        params = sys.argv[i+4:i+num_params]      # Any additional parameters, up to 3, for the effect

        # Change the appropriate part of the array by running it through the function
        pixels = pixels[0:begin] + effect_dict[name](pixels[begin:end], bc, params) + pixels[end:len(pixels)]

    print(pixels)

    time.sleep(0.5)


