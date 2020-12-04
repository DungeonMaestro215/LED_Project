from fill import fill

### Flash between the colors given as input ###
def flash(info, bc, speed, *colors):
    # Check to see if lengths of colors is divisible by 3 
    # (every color needs r, g, and b)
    if len(colors) == 0 or len(colors) % 3:
        raise Exception("Flash colors argument not of the correct size.")
    # Make sure arguments are the appropriate types
    bc = float(bc)
    speed = int(speed)
    colors = [int(c) for c in colors]

    # Which color is the current idx?
    idx = (info[1] % (len(colors) / 3)) * 3
    return fill(info, bc, colors[idx], *colors[idx:idx+3])
    # return fill(info, bc, colors[idx], colors[idx+1], colors[idx+2])