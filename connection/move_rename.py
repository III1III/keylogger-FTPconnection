import shutil
import random
import time

while True:
    file_path = "C:\example\file.exe"
    hidden_folder = "C:\example\hidden_folder"
    hidden_path = hidden_folder + "\\" + str(random.randint(1,100)) + "file.exe"
    shutil.move(file_path, hidden_path)
    time.sleep(180)
