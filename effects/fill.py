### Fills pixels with a solid color ### 
def fill(info, bc, r, g, b):
    # Make sure arguments are the appropriate types
    bc = float(bc)
    r, g, b = map(int, [r, g, b])
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

    # Put them all together and adjust for brightness
    fill_color = [int(x*bc) for x in [r, g, b]]

    # Replace each pixel with this color
    return [fill_color]*len(info[0])
