import sys
import time

# Import effects to test
from fill import fill

# Test functions
def addOne(pixels, bc, p1, p2):
    print('bc: ' + bc)
    print('p1: ' + p1)
    print('p2: ' + p2)
    return [x+1 for x in pixels]

def multTwo(pixels, bc, p1):
    print('bc: ' + bc)
    print('p1: ' + p1)
    return [x*2 for x in pixels]

function_dict = { 'addOne':addOne, 'multTwo':multTwo, 'fill':fill }

pixels = [1]*5

### Master Loop ###
try:
    while True:
        i = 1
        while (i < len(sys.argv)):
            # Gather necessary information about the effect
            # name of effect, beginning and ending index for effect on the pixel array
            name = sys.argv[i]
            i += 1
            begin, end = map(int, sys.argv[i:i+2])
            i += 2
    
            # Determine the number of extra parameters given for the effect
            j = i
            while (j < len(sys.argv) and sys.argv[j] not in function_dict):
                j += 1
    
            # Change the appropriate part of the array by running it through the function
            try:
                pixels = pixels[0:begin] + function_dict[name](pixels[begin:end], *sys.argv[i:j]) + pixels[end:len(pixels)]
            except TypeError:
                print("Error: Too many parameters given for effect '" + name + ".' Check that the correct number of parameters are given and that there are no typos.")
            i = j
        print(pixels)
    
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n\nExiting program...")
