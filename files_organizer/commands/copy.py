import shutil
import os
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger
from organize_util import loading_animation, render_screen_copy
import platform

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"spam")
destination = os.path.join(desktop,"marley")

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


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
            logger.warning("function [copy(feat=None)]")
            raise Exception("copy() - (feat=None) 0 feature in use")
            
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")

def copy_selected(name=None,ext=None,source_dir=None,dest_dir=None,feat=None):
    try:
        if check_fd_status(source_dir):
            print()
            if feat == "sub":
                for root,dirs,files in os.walk(source_dir):
                    for file in files:
                        if file.endswith(ext) and name in file:
                            source_path = os.path.join(root,file)

                            relative_path = os.path.relpath(source_path, source_dir)
                            dest_path = os.path.join(dest_dir,relative_path)
                            shutil.copy(source_path,dest_path)
                            logger.info(f"Copied Selected File :[{source_path}] to Destination : [{dest_path}]")

            elif feat == "top":
                for file in os.listdir(source_dir):
                    if file.endswith(ext) and name in file:
                        source_path = os.path.join(source_dir,file)

                        relative_path = os.path.relpath(source_path, source_dir)
                        dest_path = os.path.join(dest_dir,relative_path)
                        shutil.copy(source_path,dest_path)
                        logger.info(f"Copied Selected File :[{source_path}] to Destination : [{dest_path}]")

            else:
                logger.warning("function [copy_selected(feat=None)]")
                raise Exception("copy_selected() - (feat=None) 0 feature in use")
            
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")


def copy_main():
    while True:
        clear_screen()
        render_screen_copy()
        user_input = input("""                  
    OPT Input : """)
        print()

        if user_input not in ['0','1','2','3']:
            print("Invalid Option")
            
        if user_input == "0":
            clear_screen()

            loading_animation("Exiting Copy...", 3)

            break

        elif user_input == "1":
            source = input("Source Path(File) : ")
            dest = input("Destination Path(Dir) : ")
            copy("file",source,dest)

        elif user_input == "2":
            source = input("Source Path(Dir) : ")
            dest = input("Destination Path(Dir) : ")
            copy("dir",None,None,source,dest)

        elif user_input == "3":
            feat = input("""
[1] Top Level (Ignore Sub Dir(s))
[2] Sub Level (Entire Sub Dir(s)Tree) 
        
        OPT Input : """)
            print()

            if feat == "1":
                name = input("File Name : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                dest = input("Destination Path(Dir) : ")
                copy_selected(name,ext,source,dest,"top")
            elif feat == "2":
                name = input("File Name : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                dest = input("Destination Path(Dir) : ")
                copy_selected(name,ext,source,dest,"sub")

        print()
        input("Press Enter to Continue...")

if __name__=="__main__":
    #copy("dir",None,None,source,destination)
    #copy("file",source,destination)
    pass