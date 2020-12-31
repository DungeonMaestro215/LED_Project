import numpy as np

# adapted from https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectFire
### Fire ###
def fire(heat, pixels, frame, bc, cooling, sparking, invert, speed):
    # Validate input types
    num_pixels = len(pixels)
    if (heat == None):
        heat = [0] * num_pixels
    else:
        heat = heat[0]
    frame = int(frame)
    bc = float(bc)
    cooling = int(cooling)
    sparking = int(sparking)
    speed = float(speed)

    # Make array that tracks pixel heat
    cooldown = 0

    # Step 1. Cool down every cell a little
    for i in range(0, num_pixels):
        cooldown = np.random.randint(0, round((cooling * 10) / num_pixels) + 2)

        if (cooldown > heat[i]):
            heat[i] = 0
        else:
            heat[i] = heat[i] - cooldown

    # Step 2. Heat from each cell drifts 'up' and diffuses a little
    for k in range(num_pixels - 1, 1, -1):
        heat[k] = int((heat[k - 1] + heat[k - 2] + heat[k - 2]) / 3)

    # Step 3. Randomly ignite new 'sparks' near bottom
    spark_range = round(num_pixels / 6)
    if (np.random.randint(0, 255) < sparking):
        y = np.random.randint(0, spark_range)
        heat[y] = heat[y] + np.random.randint(160, 255)

    # Step 4. Convert heat to LED colors
    for j in range(0, num_pixels):
        if (invert == 'True'):
            id = num_pixels - 1 - j
        else:
            id = j
        # Scale 'heat' down from 0-255 to 0-191
        t192 = round((heat[j] / 255.0) * 191)

        # calculate ramp up from
        heatramp = t192 & 0x3F  # 0..63
        heatramp <<= 2  # scale up to 0..252

        # Figure out which third of the spectrum we're in
        if (t192 > 0x80):           # hottest
            pixels[id] = (255, 255, heatramp)
        elif (t192 > 0x40):         # middle
            pixels[id] = (255, heatramp, 0)
        else:                       #coolest
            pixels[id] = (heatramp, 0, 0)

    return [pixels, heat]