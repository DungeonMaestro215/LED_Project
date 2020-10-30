import sys
#import time
#import numpy as np
#
from header import header
from montecarlo import montecarlo
from fire import fire
from control import control
from meteor import meteor

effect = ""
try:
    effect = sys.argv[1]
except IndexError:
    print("")

# Initialize Pixels
num_pixels, pixels = header(300)

if (effect == "montecarlo"):
    montecarlo(num_pixels, pixels)
elif (effect == "fire"):
    fire(num_pixels, pixels)
elif (effect == "control"):
    control(num_pixels, pixels)
elif (effect == "meteor"):
    meteor(num_pixels, pixels)
