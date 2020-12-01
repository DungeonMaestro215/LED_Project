import sys

# How many arguments will each effect have?
# brightness, beginning, ending, plus 3 extra
num_params = 6

### Get inputs for each effect ###
#effects = float(sys.argv[::num_params])
#params = []

### Master Loop ###
while True:
    for effect in sys.argv[::num_params]:
        print(effect)
