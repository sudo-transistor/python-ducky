# python-ducky
new pico-ducky repository, uses python for scripting instead of duckyscript. Inspired by dbisu pico-ducky repo

# installation
1. clone repository
2. flash nuke_universal to your raspberry pi pico (any)
3. flash circuit python to the pico
  * link: https://circuitpython.org/downloads
4. replace lib folder on CIRCUITPYTHON with repo lib folder
5. copy boot.py to root of CIRCUITPYTHON
6. copy safe.py root of CIRCUITPYTHON
7. copy code.py to root of CIRCUITPYTHON

# scripting
You can write your own scripts in the code.py file using the [Adafruit HID library](https://docs.circuitpython.org/projects/hid/en/latest/)
Everything in code.py should be setup for you, please report any bugs.
there are 2 scripts pre loaded, "hydra" for password cracking (not really, just a test) and "rickroll", I think you can guess what that does ;)

# safe mode
Bridge pins 1-3 (GP0 to GND) to enter safe mode. This will allow you to edit your code with the [Circuitpython code editor](https://code.circuitpython.org/)
Otherwise, your script will run on boot.
