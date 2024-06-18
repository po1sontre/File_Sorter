# File_Sorter
Certainly, here's the updated README with a section on using PyInstaller to create an executable:

**File Sorter**

This Python script helps you organize your files by automatically sorting them into predefined categories based on their extensions.

**Features:**

- Sorts files based on their extensions (e.g., images, documents, code, etc.)
- Customizable file type dictionary for adding new categories
- Handles files with no extensions (optional)
- Skips folders (optional folder handling can be implemented)
- User-friendly interface with path input

**Installation (Optional - for Users without Python)**

If you don't have Python installed, you can download the pre-compiled executable file (`.exe` for Windows) from the [Releases](https://github.com/po1sontre/File_Sorter/releases) section of this repository. Double-click the `.exe` file to run the program.

**Usage (Python Installation Required)**

1. Clone this repository or download the source code.
2. Install the required libraries (`shutil`, `os`) using `pip install shutil os`.
3. Open a terminal or command prompt and navigate to the directory containing the script (`main.py`).
4. **To run the script:**
   - Type `python main.py` for direct execution.
5. **To create an executable (requires PyInstaller):**
   - Install PyInstaller using `pip install pyinstaller`.
   - Navigate to the directory containing `main.py`.
   - Run `pyinstaller --onefile main.py` (replace `main.py` with your script name if different).
   - This will create a new folder called `dist` (or `build` on macOS/Linux) containing the executable file (e.g., `main.exe` on Windows).

**Customization**

You can customize the file type dictionary (`filetypes`) in the `main.py` script to add new categories for specific file extensions. For example:

```python
filetypes = {
    # ... existing file types ...
    ".flac": "audio",  # Add FLAC audio files
    ".epub": "ebooks",  # Add ebooks
}
```

**Optional Folder Handling**

Currently, the script skips folders. You can modify the script to handle folders in various ways:

- Print a message indicating skipped folders.
- Implement recursive sorting within folders to organize files inside them.

**Contributing**

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit a pull request.

**License**

This project is licensed under the MIT License (see LICENSE file for details).

**Author**

Po1sontre
