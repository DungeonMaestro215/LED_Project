import numpy as np

### Randomly assign a color to every LED ### 
# change_prob - probability that any given light will change on the next frame
# off_prob - probability that any given light will turn off
# This is nice to be able to control, rather than just having one of the possible colors be 'off'
def rng(info, bc, change_prob, off_prob):
    # Validate types for inputs
    # bc, change_prob, off_prob = [float(x for x in [bc, change_prob, off_prob])]
    num_pixels = len(info[0])
    bc = float(bc)
    change_prob = float(change_prob)
    off_prob = float(off_prob)
    # Loop through each pixel
    pixels = [[0, 0, 0]] * num_pixels
    for i in range(0, num_pixels):
        # Turn this pixel off?
        if (np.random.rand(1)[0] <= off_prob):
            pixels[i] = [0, 0, 0]
        # Change this pixel's color?
        elif (np.random.rand(1)[0] <= change_prob):
            # Choose random color and scale by brightness
            colors = np.random.rand(3)
            pixels[i] = [int(bc * 255 * c) for c in colors]

    return pixels