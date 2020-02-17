# led-clock

## Changelog:

v1.2 CURRENT - switched development to a virtual environment from system-wide 
interpreter for better package management and created the requirements.txt 
file to go along with this change - 17/02/2020

v1.1 - fleshed out the README.md file - 17/02/2020

v1.0 - uploaded the files to github and created the standard github 
files. - 17/02/2020

v0.2 - wrote the most of the clock.py version of the software demo 
with the seperated clockscript.py as a background script. - 04/01/2020

v0.1 - completed the testing.py version of the software demo. - 12/12/2019

## Running the latest version of the software demo:

With Python 3 (3.7 is tested version), run the clock.py file with the
clockscript.py file in the same directory.

## The Files

### testing.py

The first version of the software based demo, all runs within one file.
Written whilst testing all the functions of the demo that I knew
would be needed. 

### clockscript.py

The background script the checks the time and generates the colours for 
the LEDs of the clock. I separated these functions from the tkinter 
visualisation code so that it can be run headlessly when deployed in the clock.

### clock.py

A neater version of the visualisation parts of the code from testing.py 
with a nicer look of the visualisation: closer together lights, better 
default colours for the clock digits and background.
