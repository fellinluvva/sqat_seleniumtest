import logging
import os


def get_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/test_execution.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
