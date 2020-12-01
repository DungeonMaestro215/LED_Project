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

pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
        )

size = 300
speed = 8
explength = int((20 + size * .4) * (1 + speed * .15))
pause = 3
vibrancy = .75

def Sparkle(length, pixel, rightc, leftc):
    # Upon meeting, expand outward
    for i in range(2, length, speed):
        pixels.fill((0, 0, 0))
        dimmer = ((length - i)/length)**2
        for j in range(0, i):
            if (pixel - j >= 0 and np.random.randint(0, int(length)) > length**(i/length)):
                if (np.random.rand() > .5):
                    pixels[pixel - j] = tuple(int(i*dimmer) for i in rightc)
                else:
                    pixels[pixel - j] = tuple(int(i*dimmer) for i in leftc)

            if (pixel + 1 + j < num_pixels and np.random.randint(0, int(length)) > i):
                if (np.random.rand() > .5):
                    pixels[pixel + 1 + j] = tuple(int(i*dimmer) for i in rightc)
                else:
                    pixels[pixel + 1 + j] = tuple(int(i*dimmer) for i in leftc)
        pixels.show()
        time.sleep(.01)
    pixels.fill((0, 0, 0))
    pixels.show()

def PrettyColors(rand, lowerbound, upperbound):
    r = 0
    g = 0
    b = 0
    # rand = np.random.rand()
    if (rand < 1):
        r = np.random.randint(lowerbound, 256)
        g = np.random.randint(lowerbound, 256)
        b = np.random.randint(0, upperbound)

    elif (rand < 2):
        r = np.random.randint(lowerbound, 256)
        g = np.random.randint(0, upperbound)
        b = np.random.randint(lowerbound, 256)

    elif (rand < 3):
        r = np.random.randint(0, upperbound)
        g = np.random.randint(lowerbound, 256)
        b = np.random.randint(lowerbound, 256)

    elif (rand < 4):
        r = np.random.randint(lowerbound, 256)
        g = np.random.randint(0, upperbound)
        b = np.random.randint(0, upperbound)

    elif (rand < 5):
        r = np.random.randint(0, upperbound)
        g = np.random.randint(lowerbound, 256)
        b = np.random.randint(0, upperbound)

    else:
        r = np.random.randint(0, upperbound)
        g = np.random.randint(0, upperbound)
        b = np.random.randint(lowerbound, 256)

    return (r, g, b)

while True:
    # c1 = tuple(np.random.randint(0, int(256)) for i in range(0, 3))
    # c2 = tuple(np.random.randint(0, int(256)) for i in range(0, 3))
    upperbound = int(255 * (1 - vibrancy))
    lowerbound = max(int(255 * vibrancy), 1)
    rand = int(np.random.rand() * 6)
    c1 = PrettyColors(rand, lowerbound, upperbound)
    rand2 = int(np.random.rand() * 6)
    while (rand2 == rand):
        rand2 = int(np.random.rand() * 6)
    c2 = PrettyColors(rand2, lowerbound, upperbound)

    # Two lines move at each other and meet in middle
    leftrand = 0
    rightrand = 0
    if (np.random.rand() > .5):
        leftrand = np.random.randint(0, int(num_pixels/1.25))
    else:
        rightrand = np.random.randint(0, int(num_pixels/1.25))

    middle = int((rightrand - leftrand + num_pixels - 1)/2)

    leftidx = 0
    rightidx = 0
    for i in range(0, num_pixels + size * 2, speed):
        pixels.fill((0, 0, 0))

        leftidx = i - leftrand
        rightidx = num_pixels - i - 1 + rightrand
        for j in range(0, size):
            if (leftidx - j >= 0 and leftidx - j <= rightidx + j):
                pixels[leftidx - j] = c1
            if (rightidx + j < num_pixels and leftidx - j < rightidx + j):
                pixels[rightidx + j] = c2

        if (leftidx - size >= rightidx + size):
            break

        pixels.show()
        time.sleep(.01)

    Sparkle(explength, middle, c1, c2)
    time.sleep(np.random.rand() * pause)
