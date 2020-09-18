import time
import board
import neopixel

pixel_pin = board.D12

num_pixels = 150

ORDER = neopixels.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness = 0.2, auto_write=False, pixel_order = ORDER
)

while True:
    print('hello')
