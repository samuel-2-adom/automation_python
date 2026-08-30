import shutil
import os
from organize_util import check_f_status,check_d_status
from organize_util import setup_logger

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"spam")
destination = os.path.join(desktop,"marley")

def copy(feat=None,source_f=None,dest_f=None,source_dir=None,dest_dir=None):
    try:
        if feat=="file":
            if check_f_status(source_f,dest_f):
                print()
                shutil.copy(source_f,dest_f)
                logger.info(f"Copied File :[{source_f}] to Destination :[{dest_f}]")
                
        elif feat=="dir":
            if check_d_status(source_dir,dest_dir):
                print()
                shutil.copytree(source_dir,dest_dir,dirs_exist_ok=True)
                logger.info(f"Copied Dir:[{source_dir}] to Destination :[{dest_dir}]")
        
        else:
            logger.warning("function [move(feat=None)]")
            raise Exception("copy() - (feat=None) 0 feature in use")
            
    except Exception as e:
        print()
        logger.error(f"Exception - {e}")
        print(f"An Exception occured : [{e}]")

if __name__=="__main__":
    #copy("dir",None,None,source,destination)
    #copy("file",source,destination)