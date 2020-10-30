def header(num):
    import board
    import neopixel
    
    # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
    # NeoPixels must be connected to D10, D12, D18 or D21 to work.
    pixel_pin = board.D12
    
    # The number of Pixels
    num_pixels = num
    
    # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
    # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
    ORDER = neopixel.GRB
    
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.6, auto_write=False, pixel_order=ORDER
    )

    return (num_pixels, pixels)
