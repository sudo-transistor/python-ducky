# python-ducky
new pico-ducky repository, uses python for scripting instead of duckyscript

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
