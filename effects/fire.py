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
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

eff_num_pixels = 40
heat = [0] * eff_num_pixels
def Fire(Cooling, Sparking, SpeedDelay):
    # Make an array that tracks pixel heat
    cooldown = 0

    # Step 1. Cool down every cell a little
    for i in range(0, eff_num_pixels):
        cooldown = np.random.randint(0, round((Cooling * 10) / eff_num_pixels) + 2)

        if (cooldown > heat[i]):
            heat[i] = 0
        else:
            heat[i] = heat[i] - cooldown

    # Step 2. Heat from each cell drifts 'up' and diffuses a little
    for k in range(eff_num_pixels - 1, 1, -1):
        heat[k] = int((heat[k - 1] + heat[k - 2] + heat[k - 2]) / 3)

    # Step 3. Randomly ignite new 'sparks' near bottom
    if (np.random.randint(0, 255) < Sparking):
        y = np.random.randint(0, 7)
        heat[y] = heat[y] + np.random.randint(160, 255)

    # Step 4. Convert heat to LED colors
    for j in range(0, eff_num_pixels):
        setPixelHeatColor(num_pixels - 1 - j, heat[j])
    
    pixels.show()
    time.sleep(SpeedDelay)

def setPixelHeatColor (Pixel, temp):
    # Scale 'heat' down from 0-255 to 0-191
    t192 = round((temp / 255.0) * 191)

    # calculate ramp up from
    heatramp = t192 & 0x3F  # 0..63
    heatramp <<= 2  # scale up to 0..252

    # Figure out which third of the spectrum we're in
    if (t192 > 0x80):           # hottest
        pixels[Pixel] = (255, 255, heatramp)
    elif (t192 > 0x40):         # middle
        pixels[Pixel] = (255, heatramp, 0)
    else:                       #coolest
        pixels[Pixel] = (heatramp, 0, 0)


while True:
    Fire(70, 40, .05)
