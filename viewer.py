import os

LOG_FILE = "secure_log.txt"

def view_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return

    print("\n======= KEYSTROKE LOGS =======\n")
    with open(LOG_FILE, "r") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    view_logs()
