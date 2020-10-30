# credit to https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectFire
def fire(num_pixels, pixels):
    import sys
    import time
    import numpy as np
    
    eff_num_pixels = 40
    try:
        effin = int(sys.argv[2])
        if (effin <= num_pixels and effin > 0):
            eff_num_pixels = effin
    except IndexError:
        print("")
    

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
        spark_range = round(eff_num_pixels / 6)
        if (np.random.randint(0, 255) < Sparking):
            y = np.random.randint(0, spark_range)
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
