import os
import shutil
path = input("Paste the file directory: ")
filetypes = {
    # Images
    ".jpg": "images",
    ".png": "images",
    ".jpeg": "images",
    ".gif": "images",
    ".bmp": "images",
    ".tiff": "images",
    ".psd": "images",
    ".pdn": "images",

    # Documents
    ".doc": "documents",
    ".txt": "documents",
    ".pdf": "documents",
    ".docx": "documents",
    ".xls": "documents",
    ".xlsx": "documents",
    ".ppt": "documents",
    ".pptx": "documents",
    ".odt": "documents",
    ".ods": "documents",
    ". odp": "documents",

    # Archives
    ".zip": "compressed",
    ".rar": "compressed",
    ".7z": "compressed",
    ".tar": "compressed",
    ".gz": "compressed",
    ".bzip2": "compressed",

    # Code
    ".c": "code",
    ".py": "code",
    ".java": "code",
    ".js": "code",
    ".cpp": "code",
    ".h": "code",
    ".cs": "code",
    ".php": "code",
    ".sh": "code",
    ".rb": "code",

    # Web
    ".html": "web",
    ".css": "web",
    ".js": "web",  # Duplicate for web development
    ".webp": "web",

    # Executables
    ".exe": "executables",
    ".msi": "executables",
    ".app": "executables",  # macOS applications

    # Data
    ".csv": "data",
    ".json": "data",
    ".xml": "data",

    # Fonts
    ".ttf": "fonts",
    ".otf": "fonts",
    ".woff": "fonts",
    ".woff2": "fonts",

    # Media
    ".mp4": "media",
    ".mov": "media",
    ".mkv": "media",
    ".avi": "media",
    ".wmv": "media",
    ".mp3": "media",
    ".wav": "media",
    ".flac": "media",
    ".ogg": "media",
    ".webm": "media",
    ".vlc": "media",  # VLC media playlist
    ".mid": "media",  # MIDI music file

    # Others
    ".bat": "scripts",
    ".lnk": "shortcuts",
    ".txt": "text",  # Duplicate for plain text files
    ".xpi": "unknown",  # Added .xpi extension
    ".dll": "dlls",     # Added .dll extension
    # 3D Models
    ".obj": "models",  # 3D object format
    # Disc Images
    ".iso": "discs",  # Disc image format (CD, DVD, etc.)
    ".amc": "unknown",
}
# Function to sort files
def sortfiles(path, filetypes):
    for filename in os.listdir(path):
        if os.path.isdir(os.path.join(path, filename)):
            print(f"Skipping folder: {filename}")
            continue 

        ex = os.path.splitext(filename)[1].lower()
        if ex in filetypes:
            destdir = os.path.join(path, filetypes[ex])
            os.makedirs(destdir, exist_ok=True)  # Creates destination folder if it doesn't exist

            sfile = os.path.join(path, filename)
            destfile = os.path.join(destdir, filename)
            shutil.move(sfile, destfile)
        else:
            print(f"Unknown file type: {filename}")

sortfiles(path, filetypes)

print("Sorting complete thank you")
