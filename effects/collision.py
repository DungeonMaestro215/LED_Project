import numpy as np
### A beam is ejected at each of the two ends of the strand.
### These meet in the middle with a cool animation.
### The respective times of these ejects is randomly determined,
### changing where they meet on the strand.

# First, a method that makes good colors
def PrettyColors(rand, lowerbound, upperbound):
    r, g, b = [0, 0, 0]

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

    return [r, g, b]


def collision(info, pixels, frame, bc, speed, pause, vibrancy):
    # testing info
    if (info == None):
        info = 0
    else:
        info = info[0]

    # Validate input types
    frame = int(frame)
    bc = float(bc)
    speed = int(speed)
    pause = int(pause)
    vibrancy = float(vibrancy)

    # Generate two nice-looking colors (thanks Simon)
    upperbound = int(255 * (1 - vibrancy))
    lowerbound = max(int(255 * vibrancy), 1)
    rand = int(np.random.rand() * 6)
    c1 = PrettyColors(rand, lowerbound, upperbound)
    rand2 = int(np.random.rand() * 6)
    while (rand2 == rand):
        rand2 = int(np.random.rand() * 6)
    c2 = PrettyColors(rand2, lowerbound, upperbound)

    return [pixels, info + 1]
    