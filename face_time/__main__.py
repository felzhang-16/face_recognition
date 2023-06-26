import multiprocessing

from face_time.src.config import UIOpenMode
from face_time.src.ui import start_web_app


if __name__ == "__main__":
    # when use pyinstaller convert .py to .exe
    # On Windows calling this function is necessary.
    # since this is multiprocessing code
    # refer to https://stackoverflow.com/questions/24944558/pyinstaller-built-windows-exe-fails-with-multiprocessing
    multiprocessing.freeze_support()
    start_web_app(UIOpenMode.CHROME)
