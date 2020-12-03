# credit to https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectMeteorRain
def meteor(num_pixels, pixels):
    import time
    import numpy as np
    
    def meteorRain(red, green, blue, meteorSize, meteorTrailDecay, meteorRandomDecay, speedDelay):
        pixels.fill((0, 0, 0))
    
        for i in range(2 * num_pixels):
            # Fade brightness 
            for j in range(num_pixels):
                if not meteorRandomDecay or np.random.random() > .5:
                    fadeToBlack(j, meteorTrailDecay)
    
            # Draw meteor
            for j in range(meteorSize):
                if i - j < num_pixels and i - j > 0:
                    pixels[i - j] = (red, green, blue)
    
            pixels.show()
            time.sleep(speedDelay)

    def fadeToBlack(pix, fadeValue):
        (r, g, b) = pixels[pix]
        r = 0 if r <= 10 else int(r - r*fadeValue/256)
        g = 0 if g <= 10 else int(g - g*fadeValue/256)
        b = 0 if b <= 10 else int(b - b*fadeValue/256)
        pixels[pix] = (r, g, b)

    while True:
        meteorRain(0x40, 0xff, 0x80, 1, 80, True, .01)
