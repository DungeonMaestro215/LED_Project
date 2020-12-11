# Individually Addressable LED Project

This repository was made to hold of the programs that control the LEDs in my living room.

By communicating with my Raspberry Pi Zero via a browser-based GUI or directly through ssh, I am able to produce different patterns on my LED strip.


TODO:
*** When transferring to Pi ***
* Uncomment mentions of 'board' and 'neopixel' in python scripts
* Change 'exec' commands
* Test running effects with "auto-write=True" and no "pixels.show()"

* Optimize for mobile (!)
* Make new gui
* Test running python scripts from Node backend
* Fire and Collisions
* Meteor speed (slower by skipping frames, or faster by increasing distance of the newly drawn meteor)
* Saving configurations

Default calls for effects (which work!)
fill:
main.py 0 fill 3 7 1 150 150 150

flash:
main.py 0 flash 3 7 1 3 0 0 0 1 1 1 2 2 2

meteor:
main.py 0 meteor 0 10 2 20 20 20 1 80 True 1