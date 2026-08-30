import shutil
import os
from pathlib import Path
import send2trash
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"db")
destination = os.path.join(desktop,"marley")


def trash(path):
    path = Path(path)
    if check_fd_status(path):
        print()
        send2trash.send2trash(path)
        logger.info(f"Sent to Trash...Path :[{path}]")

if __name__=="__main__":
    #trash(source)
        
        
    
    
    