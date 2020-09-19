def control(num_pixels, pixels):
    import sys
    
    idx = -1
    r = 0
    g = 0
    b = 0
    try:
        idx_ = int(sys.argv[2])
        r_ = int(sys.argv[3])
        g_ = int(sys.argv[4])
        b_ = int(sys.argv[5])
        if (idx_ <= num_pixels and idx_ >= 0):
            idx = idx_
        if (r_ <= 255 and r_ >= 0):
            r = r_
        if (g_ <= 255 and g_ >= 0):
            g = g_
        if (b_ <= 255 and b_ >= 0):
            b = b_
    except IndexError:
        print("")
    
    if (idx != -1):
        pixels[idx] = (r, g, b)
        pixels.show()
