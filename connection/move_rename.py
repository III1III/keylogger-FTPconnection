import shutil

file_path = "C:\example\file.exe"
hidden_path = "C:\example\hidden_folder\file.exe"

shutil.move(file_path, hidden_path)
