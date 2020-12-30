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
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)
 
# credit to https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectTheatreChase

colors = [ (220, 70, 35), (158, 8, 148), (0, 0, 0) ]
 
width = 5

while True:
    for j in range(0, 10):
        for q in range(0, width):
            for i in range(0, num_pixels, width):
                pixels[i + q] = colors[1] if (i / width) % 2 == 0 else colors[0]

            pixels.show()
            time.sleep(.02)

            for i in range(0, num_pixels, width):
                pixels[i + q] = colors[2]


