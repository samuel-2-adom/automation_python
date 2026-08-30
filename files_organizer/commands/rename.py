import shutil
import os
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger
from pathlib import Path

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"db")
dest = os.path.join(desktop,"db1")

def rename(source_path,dest_path):
    try:
        source_path = Path(source_path)
        dest_path = Path(dest_path)
        
        if check_fd_status(source_path):
            if source_path.parent != dest_path.parent:
                raise Exception("[Source/Destination] must have the Same Parent [Path/Directory]")
            else:
                shutil.move(source_path,dest_path)
                logger.info(f"Path Renamed To ... :[{dest_path}]")
    except Exception as e:
        logger.error(f"Exception - {e}")
        print(f"An Exception occured : [{e}]")