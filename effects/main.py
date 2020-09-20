import sys
import board
import neopixel


# Set up Pixels Object =======================================================

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12

# The number of Pixels
num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
# ============================================================================

# Import Effect Functions ====================================================

from montecarlo import montecarlo
from fire import fire
from control import control

# ============================================================================

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
