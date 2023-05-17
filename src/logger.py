from typing import Callable
import io
import logging
import eel


Logger = logging.getLogger("face_recognition")
Logger.setLevel("INFO")


class ForwardToFunctionStream(io.TextIOBase):
    def __init__(self, output_function: Callable = print):
        self.output_function = output_function

    def write(self, string: str) -> int:
        self.output_function(string)
        return len(string)


def add_logger_handler(logger: logging.Logger, outputer: Callable) -> None:
    handler = logging.StreamHandler(ForwardToFunctionStream(outputer))
    handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)-8s: %(message)s", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)


def log_to_ui_output(message: str) -> None:
    eel.putMessageInOutput(message)()
