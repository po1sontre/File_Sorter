import os
import shutil
import tkinter as tk
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()

path = filedialog.askdirectory(title="Select Folder")

if not path:
    print("No folder selected, exiting...")
    exit()

with open("filetypes.json", "r") as f:
    filetypes = json.load(f)

def sortfiles(path, filetypes):
    folders_dir = os.path.join(path, "folders")
    os.makedirs(folders_dir, exist_ok=True)

    organized_dirs = set(filetypes.keys())

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if full_path == folders_dir or filename in organized_dirs:
            continue

        if os.path.isdir(full_path):
            shutil.move(full_path, os.path.join(folders_dir, filename))
            print(f"Moved folder '{filename}' to 'folders'")
        else:
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in filetypes.items():
                if ext in extensions:
                    destdir = os.path.join(path, category)
                    os.makedirs(destdir, exist_ok=True)
                    shutil.move(full_path, os.path.join(destdir, filename))
                    break
            else:
                print(f"Unknown file type: {filename}")

sortfiles(path, filetypes)
print("Sorting complete.")
