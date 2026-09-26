import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_name="api_client.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_f = logging.Formatter("%(name)s | %(levelname)s | %(message)s")
    file_f = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_f)

    file_handler = RotatingFileHandler(log_name, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_f)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger(__name__)
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")