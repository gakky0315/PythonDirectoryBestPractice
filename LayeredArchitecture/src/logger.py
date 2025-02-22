import logging
import sys

def get_logger(name="app_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    if not logger.hasHandlers():
        logger.addHandler(handler)
    
    return logger
