from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename


def ask_folder() -> str | None:
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    folder = askdirectory(parent=root)
    root.update()

    return folder if bool(folder) else None


def ask_file(file_type):
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

    # bool(file_path) will help filter our the negative cases; an empty string or an empty tuple
    return file_path if bool(file_path) else None
