# Individually Addressable LED Project

This repository was made to hold of the programs that control the LEDs in my living room.

By communicating with my Raspberry Pi Zero via a browser-based GUI or directly through ssh, I am able to produce different patterns on my LED strip.


TODO:
*** When transferring to Pi ***
* Uncomment mentions of 'board' and 'neopixel' in python scripts
* Make sure correct versions of packages (numpy)
* Change 'spawn' commands
* Test running effects with "auto-write=True" and no "pixels.show()"
* Don't send 'effect' in communicator
* Remove frame limit
* Rainbow needs testing

*** Coding ***
* Move where the settings are bound *** 
* Optimize effects...
    * Make special 'info' effects?
* Meteor checkbox doesn't reflect effect's settings
* Optimize for mobile (!)
* Fire and Collisions effects
* Count down / timer
* Random explosions (fireworks)
* Meteor speed (slower by skipping frames, or faster by increasing distance of the newly drawn meteor)
* Saving configurations
* Do something if brightness control is >1
* Multiple effects!
* Inverted Fire effect

*** Alexa Integration ??? ***
* Figure out how to make Alexa make HTTP requests
* How to handle colors? or various effects
* Create voice commands that correspond to that request

*** Audio Visualzing ***
* Get microphone?
* Copy over visualization stuff from Pi 4
* Get visualizer to work with Raspotify
* Get Raspotify and visualizer to work with bluetooth 🤢
* Need long MicroUSB to 3.5mm audio cable (?)
    * Doesn't work without sound card (looking at you Pi 0)
* Setup Neopixel for the visualizer / Use their build in Pi controls
* Create new effect with 3 equilizer bars
* Possible issues: 
    * Will it work headless...? (github says maybe not)
    * Is the refresh rate going to be okay?

Default calls for effects (which work!)
fill:
main.py 0 fill 3 7 1 150 150 150

flash:
main.py 0 flash 3 7 1 3 0 0 0 1 1 1 2 2 2

meteor:
main.py 0 meteor 0 10 1 20 20 20 1 80 True 1