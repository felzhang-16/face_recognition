import logging
import os
import pathlib

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_file = os.path.join(pathlib.Path(os.path.abspath(__file__)).parent.parent, 'syslog')
fileHandler = logging.FileHandler(log_file, mode='w')
fileHandler.setLevel(logging.DEBUG)

logger.addHandler(fileHandler)
