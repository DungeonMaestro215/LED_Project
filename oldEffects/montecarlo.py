def montecarlo(num_pixels, pixels):
    import sys
    import time
    import numpy as np
    # Brightness Control
    bc = .25     #note that 25% of the max 80% is 20%
    try:
        bcin = float(sys.argv[4])
        if (bcin <= 1 and bcin > 0):
            bc = bcin
    except IndexError:
        print("")
    
    
    # Probability that a light changes color
    prop = .33
    try:
        propin = float(sys.argv[2])
        if (propin <= 1 and propin > 0):
            prop = propin
    except IndexError:
        print("No proportion give, default 33%.")
    
    # Probability that a light turns off
    offprop = 0
    try:
        offpropin = float(sys.argv[3])
        if (offpropin < 1 and offpropin > 0):
            offprop = offpropin
    except IndexError:
        print("No off proportion give, default 0%.")
    
    while True:
        for i in range(0, num_pixels):
            if (np.random.rand(1)[0] <= offprop):
                pixels[i] = (0, 0, 0)
                continue
            if (np.random.rand(1)[0] <= prop):
                colors = np.random.rand(3)
                pixels[i] = (int(bc * 255 * colors[0]), int(bc * 255 * colors[1]), int(bc * 255 * colors[2]))
        
        pixels.show()
        time.sleep(0.1)
    
