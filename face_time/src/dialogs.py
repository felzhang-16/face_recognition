from typing import Optional

from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename


def ask_folder() -> Optional[str]:
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    folder = askdirectory(parent=root)
    root.update()

    return folder if bool(folder) else None


def ask_file(file_type: str) -> Optional[str]:
    """Ask the user to select a file"""
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    if file_type == "jpg":
        file_types = [("jpg files", "*.jpg;*.JPG;*.png;*.PNG"), ("All files", "*")]
    else:
        file_types = [("All files", "*")]
    file_path = askopenfilename(parent=root, filetypes=file_types)
    root.update()

    return file_path if bool(file_path) else None
