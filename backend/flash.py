from fill import fill

### Flash between the colors given as input ###
def flash(pixels, frame, bc, speed, *colors):
    # Check to see if lengths of colors is divisible by 3 
    # (every color needs r, g, and b)
    if len(colors) == 0 or len(colors) % 3:
        raise Exception("Flash colors argument not of the correct size.")
    # Make sure arguments are the appropriate types
    frame = int(frame)
    bc = float(bc)
    speed = int(speed)
    colors = [int(c) for c in colors]

    # Which color is the current idx?
    idx = int(frame / speed % (len(colors) / 3)) * 3
    return fill(pixels, frame, bc, *colors[idx:idx+3])