import os
from .setup_logger import setup_logger
logger = setup_logger(__name__)
from pathlib import Path

def check_f_status(source_f=None,dest_f=None):
    try:
        source_f = Path(source_f)
        dest_f = Path(dest_f)
        
        if os.path.exists(source_f):
            if os.path.isfile(source_f):
                logger.info("File Passed Status Check...")
                return True
            else:
                logger.error("File Failed Status Check...")
                raise Exception("Invalid File Path...")
                return False
        else:
            logger.error("Failed to get File Path....")
            raise Exception("File does not Exist...")
    except Exception as e:
        logger.error(f"Exception - {e}")
        print(f"An Exception Occured : {e}")

def check_d_status(source_dir=None,dest_dir=None):
    try:
        source_dir = Path(source_dir)
        dest_dir = Path(dest_dir)
        
        os.makedirs(dest_dir,exist_ok=True)
        if os.path.exists(source_dir) and os.path.exists(dest_dir):
            if os.path.isdir(source_dir) and os.path.isdir(dest_dir):
                logger.info("Directory Passed Status Check...")
                return True
            else:
                logger.error("Directory Failed Status Check...")
                raise Exception("Invalid Directory Path...")
                return False
        else:
            logger.error("Failed to get Direvtory Path....")
            raise Exception("Directory does not Exist...")

    except Exception as e:
        logger.error(f"Exception - {e}")
        print(f"An Exception Occured : {e}")

def check_fd_status(source_path):
    try:
        source_path = Path(source_path)
        if os.path.exists(source_path):
            if os.path.isfile(source_path):
                logger.info("File Passed Status Check...")
                return True
            elif os.path.isdir(source_path):
                logger.info("Directory Passed Status Check...")
                return True
            else:
                logger.error("File/Directory Failed Status Check...")
                raise Exception("Invalid File/Directory Path...")
                return False
        else:
            logger.error("Failed to Get File/Directory Path....")
            raise Exception("File/Directory Does Not Exist...")
            
    except Exception as e:
        logger.error(f"Exception - {e}")
        print(f"An Exception Occured : {e}")