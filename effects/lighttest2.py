# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12
 
# The number of NeoPixels
num_pixels = 300
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)
 
while True:
    for i in range(0, num_pixels):
        pixels.fill((0, 0, 0))
        pixels[i] = (150, 150, 150)
        pixels.show()
        time.sleep(0.01)

    for j in range (0, num_pixels):
        pixels.fill((0, 0, 0))
        pixels[num_pixels - 1 - j] = (150, 150, 150)
        pixels.show()
        time.sleep(0.01)


