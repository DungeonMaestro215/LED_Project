# Adapted from https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectMeteorRain
from numpy import random
from fill import fill

### Generate a meteor that flys across the LEDs ###
def meteor(info, bc, r, g, b, meteor_size, meteor_trail_decay, meteor_rand_decay, speed):
    pixels, frame = info
    # Make sure arguments are the appropriate types
    bc = float(bc)
    r, g, b, meteor_size, meteor_trail_decay, speed = map(int, [r, g, b, meteor_size, meteor_trail_decay, speed])
    meteor_rand_decay = meteor_rand_decay == "1" or meteor_rand_decay.lower() == "true"
    # Make sure r,g,b values are in range 0-255
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    
    # Fade brightness of all pixels
    pixels = [fadeToBlack(pix, meteor_trail_decay, not meteor_rand_decay or random.random() > .5) for pix in pixels]

    # Draw meteor
    idx = frame % len(pixels)
    pixels[idx:idx + meteor_size] = fill([pixels[idx:idx+meteor_size], frame], bc, r, g, b)

    return pixels


def fadeToBlack(pix, fade_value, rand_decay):
    if rand_decay:
        return [0 if x <= 10 else int(x - x*fade_value/256) for x in pix]
    else:
        return pix
