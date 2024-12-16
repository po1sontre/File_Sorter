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
    # Create 'folders' directory if it doesn't exist
    folders_dir = os.path.join(path, "folders")
    os.makedirs(folders_dir, exist_ok=True)

    # Keep track of the directories that are already organized
    organized_dirs = set(filetypes.keys())

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        
        # Skip the 'folders' directory and any already organized directories
        if full_path == folders_dir or filename in organized_dirs:
            continue

        # If it's a directory
        if os.path.isdir(full_path):
            # Move any unorganized folder to 'folders'
            shutil.move(full_path, os.path.join(folders_dir, filename))
            print(f"Moved folder '{filename}' to 'folders'")

        else:
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
