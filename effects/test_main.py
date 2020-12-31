### Import necessary packages ### 
import sys
import time
# import board
# import neopixel
import numpy as np

### Effects ###
### Import other effects and create effect dictionary ###
from fill import fill
from flash import flash
from meteor import meteor
from rng import rng
from rainbow import rainbow
from collision import collision
from fire import fire
from timer import timer
effect_dict = { 'fill':fill, 'flash':flash, 'meteor':meteor, 'rng':rng, 'rainbow':rainbow }
special_effect_dict = {'collision': collision, 'fire': fire, 'timer': timer}

### Set up NeoPixel pixel array ###
# Choose an open pin connected to the Data In of the NeoPixel strip
# pixel_pin = board.D12

# The number of pixels
num_pixels = 10

# The order of the pixel colors 
# ORDER = neopixel.GRB

# Set up the array for the strip
# pixels = neopixel.NeoPixel(
#         pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
#         )
pixels = [[0, 0, 0]] * num_pixels

### Effects that don't need special treatment ###
def sparkle(pixels, idx, length, speed, delay):
    for i in range(2, length, speed):
        pixels.fill((0, 0, 0))
        dimmer = ((length - i)/length)**2
        for j in range(0, i):
            r = np.random.randint(0, 256) * dimmer
            g = np.random.randint(0, 256) * dimmer
            b = np.random.randint(0, 256) * dimmer
            if (idx - j >= 0 and np.random.randint(0, int(length)) > length**(i/length)):
                pixels[idx - j] = (r, g, b)
            if (idx + 1 + j < num_pixels and np.random.randint(0, int(length)) > i):
                pixels[idx + 1 + j] = (r, g, b)

        #pixels.show()
        time.sleep(.01)
        print(pixels)

def timer2(pixels, time_length, delay):
    time_length = int(time_length)
    current_time = int(round(time.time()))
    end_time = current_time + time_length
    while (end_time > current_time):
        for i in range(0, len(pixels)):
            if (i < int(len(pixels) * (end_time - current_time) / time_length)):
                pixels[i] = [150, 150, 150]
            else:
                pixels[i] = [0, 0, 0]
        
        #pixels.show()
        print(pixels)
        time.sleep(delay)
        current_time = int(round(time.time()))

    # Fireworks when timer finishes
    length = 10
    speed = 1
    while True:
        idx = np.random.randint(0, len(pixels))
        sparkle(pixels, idx, length, speed, delay)

not_special_effects_dict = { 'timer2': timer2 }

### Master Loop ###
# First argument will indicate whether or not this is a static effect
static = sys.argv[1] == '1' or sys.argv[1].lower() == 'true' or sys.argv[1].lower() == 'static'
delay = 0.01
frame_num = 0

# Special effects may need to send data to a future frame
effect_info = {}
try:
    if (sys.argv[1] in not_special_effects_dict):
        not_special_effects_dict[sys.argv[1]](pixels, sys.argv[2], delay)
    else:
        while True:
            # Parse through input. Effect arguments start at index 2
            i = 2
            while (i < len(sys.argv)):
                # Gather necessary information about the effect
                # name of effect, beginning and ending index for effect on the pixel array
                # name = sys.argv[i]
                # i += 1
                # begin, end = map(int, sys.argv[i:i+2])
                # i += 2
                name = sys.argv[i]
                begin = int(sys.argv[i+1])
                end = int(sys.argv[i+2])
                i+=3

                # Determine the number of extra parameters given for the effect
                j = i
                while (j < len(sys.argv) and (sys.argv[j] not in effect_dict or sys.argv[j] not in special_effect_dict)):
                    j += 1
        
                # Change the appropriate part of the array by running it through the function
                try:
                    # Normal effect
                    if (name in effect_dict):
                        effect_results = effect_dict[name](pixels[begin:end], frame_num, *sys.argv[i:j])    # Call effect
                        # pixels = pixels[0:begin] + effect_results + pixels[end:len(pixels)]      # Insert effect into pixel array
                        pixels[0:num_pixels] = pixels[0:begin] + effect_results + pixels[end:len(pixels)]      # Insert effect into pixel array
                    # Special effect
                    else:
                        # Initialize an info key for this effect
                        if (frame_num == 0):
                            effect_info["" + name + str(begin)] = None
                        
                        effect_results = special_effect_dict[name](effect_info["" + name + str(begin)], pixels[begin:end], frame_num, *sys.argv[i:j])    # Call effect
                        pixels = pixels[0:begin] + effect_results[0] + pixels[end:len(pixels)]      # Insert effect into pixel array
                        effect_info["" + name + str(begin)] = effect_results[1:len(effect_results)]      # Update any given info 
                        print(effect_results[1])

                except ZeroDivisionError as e:
                    print("Error: Incorrect number of parameters given for effect '" + name + ".' Check that the correct number of parameters are given and that there are no typos.")
                    print(e)

                i = j
            print(pixels)
            sys.stdout.flush()
            # pixels.show()
            # if (static or frame_num > 10):
            if (static):
                break
        
            frame_num+=1
            time.sleep(delay)
except KeyboardInterrupt:
    print("\n\nExiting program...")
