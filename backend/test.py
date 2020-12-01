import sys
import time

# How many arguments will each effect have?
# effect name, brightness, beginning, ending, plus 3 extra is 7
num_params = 7

pixels = [1]*5

### Master Loop ###
while True:
    for i in [1:len(sys.argv):num_params]:
        print(sys.argv[i])
        # if (effect == "addOne"):
            

    time.sleep(0.5)

def addOne(pixels):
    return [x+1 for x in pixels]

def multTwo(pixels):
    return [x*2 for x in pixels]