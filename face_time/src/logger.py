from typing import Callable, Any
import io
import logging
import queue

import eel


Logger = logging.getLogger("app")
Logger.setLevel("DEBUG")


class ForwardToFunctionStream(io.TextIOBase):
    def __init__(self, output_function: Callable):
        self.output_function = output_function

    def write(self, string: str) -> int:
        self.output_function(string)
        return len(string)


def add_logger_handler(logger: logging.Logger, outputer: Callable) -> None:
    handler = logging.StreamHandler(ForwardToFunctionStream(outputer))
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s: %(funcName)s: %(message)s", "%Y-%m-%d %H:%M:%S"
        )
    )
    logger.addHandler(handler)


def log_to_ui_output(message: str) -> None:
    eel.putMessageInOutput(message)


def logger_process(queue: queue.Queue[Any], output: Callable):
    logger = logging.getLogger("app_inside")
    add_logger_handler(logger, output)
    logger.info("Logger process running...")
    while True:
        message = queue.get()
        if message is None:
            logger.info("Logger process shutting down...")
            break
        logger.handle(message)
