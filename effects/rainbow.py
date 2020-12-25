### Rainbow ###

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow(info, bc, speed):
    # Validate input types
    bc = float(bc)
    speed = int(speed)
    frame = int(info[1]) % 255
    num_pixels = len(info[0])

    # Calculate position for each LED
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels) + frame
        info[0][i] = wheel(pixel_index & 255)

    return info[0]