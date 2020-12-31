# adapted from https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectFire
### Fire ###
def fire(heat, pixels, frame, bc, cooling, sparking, speed):
    # Validate input types
    if (heat == None):
        heat = [0] * len(pixels)
    frame = int(frame)
    bc = float(bc)
    cooling = int(cooling)
    sparking = int(sparking)
    speed = int(speed)

    cooldown = 0

    # Step 1. Cool down every cell a little
    # Step 2. Heat from each cell drifts 'up' and diffuses a little
    # Step 3. Randomly ignite new 'sparks' near bottom
    # Step 4. Convert heat to LED colors

    return pixels