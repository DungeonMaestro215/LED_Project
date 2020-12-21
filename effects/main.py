### Import necessary packages ### 
import sys
import time
# import board
# import neopixel
import numpy as np

### Import effects and create effect dictionary ###
from fill import fill
from flash import flash
from meteor import meteor
effect_dict = { 'fill':fill, 'flash':flash, 'meteor':meteor }


### Set up NeoPixel pixel array ###
# Choose an open pin connected to the Data In of the NeoPixel strip
# pixel_pin = board.D12

# The number of pixels
num_pixels = 10

# The order of the pixel colors 
# ORDER = neopixel.GRB

# Set up the array for the strip
# pixels = neopixel.NeoPixel(
#         pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
#         )
pixels = [[0, 0, 0]] * num_pixels


### Master Loop ###
# First argument will indicate whether or not this is a static effect
static = sys.argv[1] == '1' or sys.argv[1].lower() == 'true' or sys.argv[1].lower() == 'static'
delay = 0.5
frame_num = 0
try:
    while True:
        # Parse through input. Effect arguments start at index 2
        i = 2
        while (i < len(sys.argv)):
            # Gather necessary information about the effect
            # name of effect, beginning and ending index for effect on the pixel array
            # name = sys.argv[i]
            # i += 1
            # begin, end = map(int, sys.argv[i:i+2])
            # i += 2
            name = sys.argv[i]
            begin = int(sys.argv[i+1])
            end = int(sys.argv[i+2])
            i+=3

            # Determine the number of extra parameters given for the effect
            j = i
            while (j < len(sys.argv) and sys.argv[j] not in effect_dict):
                j += 1
    
            # Change the appropriate part of the array by running it through the function
            # Each function will be given an 'info' array with necessary info to make the effect work
            info = [pixels[begin:end], frame_num]
            try:
                pixels = pixels[0:begin] + effect_dict[name](info, *sys.argv[i:j]) + pixels[end:len(pixels)]
            except TypeError:
                print("Error: Incorrect number of parameters given for effect '" + name + ".' Check that the correct number of parameters are given and that there are no typos.")
            i = j
        print(pixels)
        sys.stdout.flush()
        # pixels.show()
        if (static or frame_num > 10):
            break
    
        frame_num+=1
        time.sleep(delay)
except KeyboardInterrupt:
    print("\n\nExiting program...")
