### Fills pixels with a solid color ###
def fill(pixels, bc, r, g, b):
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
    
    return pixels.fill(int(x * bc) for x in (r, g, b))