from typing import Callable, Any
import io
import logging
import queue
import datetime

import eel


Logger = logging.getLogger("app")
Logger.setLevel("DEBUG")


class ForwardToFunctionStream(io.TextIOBase):
    def __init__(self, output_function: Callable):
        self.output_function = output_function

    def write(self, string: str) -> int:
        self.output_function(string)
        return len(string)


class DeltaTimeFormatter(logging.Formatter):
    def format(self, record):
        duration = datetime.datetime.utcfromtimestamp(record.relativeCreated / 1000)
        record.delta = duration.strftime("%M:%S.%f")[:-3]
        return super().format(record)


def add_logger_handler(logger: logging.Logger, outputer: Callable) -> None:
    handler = logging.StreamHandler(ForwardToFunctionStream(outputer))
    log_format = "%(delta)s:%(levelname)s:%(process)d:%(filename)s:%(lineno)s:%(funcName)s: %(message)s"
    handler.setFormatter(DeltaTimeFormatter(log_format))
    logger.addHandler(handler)


def log_to_ui_output(message: str) -> None:
    eel.putMessageInOutput(message)


def logger_thread(queue: queue.Queue[Any], output: Callable):
    logger = logging.getLogger("app_inside")
    add_logger_handler(logger, output)
    logger.info("Logger process running...")
    while True:
        message = queue.get()
        if message is None:
            logger.info("Logger process shutting down...")
            break
        logger.handle(message)
