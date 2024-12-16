# File Sorter

This Python script helps you organize your files by categorizing them based on their extensions. It automatically moves files and folders into pre-defined categories as specified in a `filetypes.json` file. The script uses a graphical file dialog to select the folder to organize.

## Features

- Automatically sorts files based on their extensions.
- Moves files into categorized folders (e.g., documents, images, scripts).
- Organizes unorganized folders into a `folders` directory.
- User-friendly interface with a file dialog for selecting directories.
- Customizable file categories via `filetypes.json`.

## Requirements

- Python 3.x
- `tkinter` (usually included in Python installations)
- `json`
- `shutil`

## Installation

1. Clone this repository or download the script files to your computer.
2. Make sure you have Python 3 installed.
3. Install any dependencies (though `tkinter` and other libraries are usually pre-installed with Python).

## Usage

1. **Prepare `filetypes.json`**: Create or modify a `filetypes.json` file to define the file types and their categories. For example:

    ```json
    {
        "documents": [".pdf", ".docx", ".txt"],
        "images": [".jpg", ".png", ".gif"],
        "scripts": [".py", ".sh", ".bat"],
        "audio": [".mp3", ".wav"]
    }
    ```

2. **Run the script**:
    - Run the script using the command line or an IDE.
    - A file dialog will open, allowing you to select the folder you wish to organize.
    - The script will sort the files and move them into the appropriate directories based on the file extensions.

    ```bash
    python main.py
    ```

3. **Sorting**: The script will:
    - Create folders for each file category defined in `filetypes.json`.
    - Move files into the appropriate folders.
    - Place any unorganized folders into a `folders` directory.

## Example Filetypes

```json
{
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "images": [".jpg", ".png", ".gif", ".bmp"],
    "audio": [".mp3", ".wav"],
    "scripts": [".py", ".sh", ".bat"]
}

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

This project was created and maintained by [po1sontre](https://github.com/po1sontre).