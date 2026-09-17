import board
import digitalio
import storage
import supervisor

# Set up a pin to act as a "switch"
write_pin = digitalio.DigitalInOut(board.GP0)
write_pin.direction = digitalio.Direction.INPUT
write_pin.pull = digitalio.Pull.UP

# If GP0 is wired to GND on start-up, CircuitPython gets write access.
# If GP0 is left disconnected, your computer keeps write access.
if not write_pin.value:
    # safe mode
    storage.remount("/", readonly=False)
    storage.disable_usb_drive()
    supervisor.set_next_code_file("safe.py")
    supervisor.reload()
else:
    # deploy payloads in code.py
    pass
