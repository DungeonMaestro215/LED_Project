import sys
import time

# Test function
def addOne(pixels):
    return [x+1 for x in pixels]

def multTwo(pixels):
    return [x*2 for x in pixels]

function_dict = { 'addOne':addOne, 'multTwo':multTwo }
# How many arguments will each effect have?
# effect name, brightness, beginning, ending, plus 3 extra is 7
num_params = 7

pixels = [1]*5

### Master Loop ###
while True:
    for i in range(1, len(sys.argv), num_params):
        name = sys.argv[i]
        bc = float(sys.argv[i + 1])
        begin = int(sys.argv[i + 2])
        end = int(sys.argv[i + 3])
        pixels = pixels[0:begin] + function_dict[name](pixels[begin:end]) + pixels[end:len(pixels)]
    print(pixels)
            

    time.sleep(0.5)

