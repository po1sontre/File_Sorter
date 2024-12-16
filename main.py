import os
import shutil
import tkinter as tk
from tkinter import filedialog
import json

# Create a root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Use file dialog to select a directory
path = filedialog.askdirectory(title="Select Folder")

if not path:
    print("No folder selected, exiting...")
    exit()

# Load file types from the updated JSON file
with open("filetypes.json", "r") as f:
    filetypes = json.load(f)

# Function to sort files
def sortfiles(path, filetypes):
    for filename in os.listdir(path):
        if os.path.isdir(os.path.join(path, filename)):
            print(f"Skipping folder: {filename}")
            continue

        ex = os.path.splitext(filename)[1].lower()
        # Loop through categories in filetypes
        for category, extensions in filetypes.items():
            if ex in extensions:
                destdir = os.path.join(path, category)
                os.makedirs(destdir, exist_ok=True)  # Create category folder if it doesn't exist

                sfile = os.path.join(path, filename)
                destfile = os.path.join(destdir, filename)
                shutil.move(sfile, destfile)
                break
        else:
            print(f"Unknown file type: {filename}")

sortfiles(path, filetypes)

print("Sorting complete, thank you!")
