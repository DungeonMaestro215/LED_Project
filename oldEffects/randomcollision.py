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
    pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=ORDER
)

size = 3

def sparkle(length, pixel):
    # Upon meeting, expand outward
    for i in range(int(size/2), int(length)):
        pixels.fill((0, 0, 0))
        dimmer = (length - i)/length
        for j in range(0, i):
            if (np.random.randint(0, int(length)) > i):
                c1 = tuple(np.random.randint(0, int(256*dimmer)) for i in range(0, 3))
                pixels[pixel - j] = c1
            if (np.random.randint(0, int(length)) > i):
                c2 = tuple(np.random.randint(0, int(256*dimmer)) for i in range(0, 3))
                pixels[pixel + 1 + j] = c2
        pixels.show()
        time.sleep(.01)

while True:
    r1 = np.random.randint(0, 256)
    g1 = np.random.randint(0, 56)
    b1 = np.random.randint(0, 56)
    r2 = np.random.randint(0, 56)
    g2 = np.random.randint(0, 56)
    b2 = np.random.randint(0, 256)

    # Two lines move at each other and meet in middle
    leftrand = 0
    rightrand = 0
    if (np.random.rand() > .5):
        leftrand = np.random.randint(0, int(num_pixels/1.25))
    else:
        rightrand = np.random.randint(0, int(num_pixels/1.25))

    middle = int((num_pixels - 1 + rightrand - leftrand)/2)
    

    leftidx = 0
    rightidx = 0
    for i in range(size - 1, num_pixels):
        pixels.fill((0, 0, 0))

        for j in range(0, size):
            leftidx = i - j - leftrand
            rightidx = num_pixels - i + j - 1 + rightrand
            if (leftidx >= 0): 
                pixels[leftidx] = (r1, g1, b1)
            if (rightidx <= num_pixels - 1):
                pixels[rightidx] = (r2, g2, b2)

        if (leftidx >= rightidx):
            break

        pixels.show()
        time.sleep(.01)
    
    sparkle(20, leftidx)
