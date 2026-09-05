import shutil
import os
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger
from organize_util import loading_animation, render_screen_move
import platform

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"Thonny","spam")
destination = os.path.join(desktop)

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def move(feat=None,source_f=None,dest_f=None,source_dir=None,dest_dir=None):
    try:
        if feat=="file":
            if check_f_status(source_f,dest_f):
                print()
                shutil.move(source_f,dest_f)
                logger.info(f"Moved File :[{source_f}] to Destination : [{dest_f}]")
                
        elif feat=="dir":
            if check_d_status(source_dir,dest_dir):
                print()
                shutil.move(source_dir,dest_dir)
                logger.info(f"Moved Dir:[{source_dir}] to Destination : [{dest_dir}]")
        
        else:
            logger.warning("function [move(feat=None)]")
            raise Exception("[move()] - (feat=None) 0 feature in use")
            
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")

def move_selected(name=None,ext=None,source_dir=None,dest_dir=None,feat=None):
    try:
        if check_fd_status(source_dir):
            print()
            if feat == "sub":
                success = False
                for root,dirs,files in os.walk(source_dir):
                    for file in files:
                        if file.endswith(ext) and name in file:
                            source_path = os.path.join(root,file)

                            relative_path = os.path.relpath(source_path, source_dir)
                            dest_path = os.path.join(dest_dir,relative_path)
                            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                            shutil.move(source_path,dest_path)
                            success = True
                            logger.info(f"Moved Selected File :[{source_path}] to Destination : [{dest_path}]")
                if not success:
                    logger.info(f"No files found with name [{name}] and extension [{ext}] in source directory [{source_dir}]")

            elif feat == "top":
                success = False
                for file in os.listdir(source_dir):
                    if file.endswith(ext) and name in file:
                        source_path = os.path.join(source_dir, file)

                        relative_path = os.path.relpath(source_path, source_dir)
                        dest_path = os.path.join(dest_dir,relative_path)
                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                        shutil.move(source_path,dest_path)
                        success = True
                        logger.info(f"Moved File :[{source_path}] to Destination : [{dest_path}]")
                if not success:
                    logger.info(f"No files found with name [{name}] and extension [{ext}] in source directory [{source_dir}]")

            else:
                logger.warning("function [move_selcted(feat=None)]")
                raise Exception("move_selected() - (feat=None) 0 feature in use")
            
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")


def move_main():
    while True:
        clear_screen()
        render_screen_move()

        user_input = input("""                  
    OPT Input : """)
        print()
        
        if user_input not in ['0','1','2','3']:
            logger.info("Invalid Option Selected")

        if user_input == "0":
            clear_screen()
            loading_animation("Exiting Move...", 1)
            break

        elif user_input == "1":
            source = input("Source Path(File) : ")
            dest = input("Destination Path(Dir) : ")
            print()
            move("file",source,dest)

        elif user_input == "2":
            source = input("Source Path(Dir) : ")
            dest = input("Destination Path(Dir) : ")
            print()
            move("dir",None,None,source,dest)

        elif user_input == "3":
            feat = input("""
[1] Top Level (Ignore Sub Dir(s))
[2] Sub Level (Entire Sub Dir(s)Tree) 
                    
        OPT Input : """)
            print()

            if feat == "1":
                name = input("File Name (no extension) : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                dest = input("Destination Path(Dir) : ")
                print()
                move_selected(name,ext,source,dest,"top")

            elif feat == "2":
                name = input("File Name (no extension) : ")
                ext = input("File Extension : ")
                source = input("Source Path(Dir) : ")
                dest = input("Destination Path(Dir) : ")
                print()
                move_selected(name,ext,source,dest,"sub")

            else:
                logger.info("Invalid Feature Selected")

        print()
        input("Press Enter to Continue...")

if __name__ == "__main__":
    #move('dir',None,None,source,destination)
    #move('file',source,destination)
    pass