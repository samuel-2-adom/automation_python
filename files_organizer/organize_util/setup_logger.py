import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name,f_name="organize_files.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter_c = logging.Formatter("%(name)s | %(levelname)s | %(message)s")
    formatter_f =  logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter_c)
    
    file_handler = RotatingFileHandler(f_name,maxBytes=1_000_000,backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_f)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger