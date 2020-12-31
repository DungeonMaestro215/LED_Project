import time

### Timer ###
def timer(end_time, pixels, frame, bc, time_length):
    # Validate inputs
    frame = int(frame)
    bc = float(bc)
    time_length = int(time_length)
    if (end_time == None):
        end_time = int(round(time.time())) + time_length
    else:
        end_time = end_time[0]

    current_time = int(round(time.time()))
    if (current_time < end_time):
        for i in range(0, int(len(pixels) * (end_time - current_time) / time_length)):
            pixels[i] = [150, 150, 150]
        for i in range(len(pixels) - 1, int(len(pixels) * (end_time - current_time) / time_length), -1):
            pixels[i] = [0, 0, 0]
    else:
        pixels[0:len(pixels)] = [255, 0, 0] * len(pixels)

    return [pixels, end_time]