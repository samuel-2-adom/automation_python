import shutil
import os
from pathlib import Path
import send2trash
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger
from organize_util import loading_animation, render_screen_trash
import platform


logger = setup_logger(__name__)


def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


def trash(path=None):
    try:

        if check_fd_status(path):
            print()
            send2trash.send2trash(path)
            logger.info(f"Sent to Trash...Path :[{path}]")
    except Exception as e:
        print(f"An Exception Occured : {e}")


def trash_selected(name=None,ext=None,source_dir=None,feat=None):
    try:
        if check_fd_status(source_dir):
            print()
            if os.path.isdir(source_dir):
                if feat == "sub":
                    success = False
                    for root,dirs,files in os.walk(source_dir):
                        for file in files:
                            if file.endswith(ext) and name in file:
                                source_path = os.path.join(root,file)
                                send2trash.send2trash(source_path)
                                success = True
                                logger.info(f"Sent to Trash...Path :[{source_path}]")
                    if not success:
                        logger.info(f"No files found with name [{name}] and extension [{ext}] in source directory [{source_dir}]")

                elif feat == "top":
                    success = False
                    for file in os.listdir(source_dir):
                        if file.endswith(ext) and name in file:
                            source_path = os.path.join(source_dir,file)
                            send2trash.send2trash(source_path)
                            success = True
                            logger.info(f"Sent to Trash...Path :[{source_path}]")
                    if not success:
                        logger.info(f"No files found with name [{name}] and extension [{ext}] in source directory [{source_dir}]")
                
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")

def trash_main():
    while True:
        clear_screen()
        render_screen_trash()
        user_input = input("""              
    OPT Input : """)
        print()
        
        if user_input not in ['0','1','2']:
            logger.info("Invalid Option Selected")
            
        if user_input == "0":
            clear_screen()
            loading_animation("Exiting Trash...", 1)
            break

        elif user_input == "1":
            path = input("Path to File/Dir : ")
            print()
            trash(path)

        elif user_input == "2":
            

            feat = input("""
[1] Top Level (Ignore Sub Dir(s))
[2] Sub Level (Entire Sub Dir(s)Tree) 
        
        OPT Input : """)
            print()
            
            if feat == "1":
                name = input("File Name (no extension) : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                print()
                trash_selected(name,ext,source,"top")

            elif feat == "2":
                name = input("File Name (no extension) : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                print()
                trash_selected(name,ext,source,"sub")

            else:
                logger.info("Invalid Feature Selected")

        print()
        input("Press Enter to Continue...")

if __name__=="__main__":
    #trash(source)
    pass