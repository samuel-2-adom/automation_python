import shutil
import os
from organize_util import check_f_status,check_d_status,check_fd_status
from organize_util import setup_logger
from organize_util import loading_animation, render_screen_rename
from pathlib import Path
import platform

logger = setup_logger(__name__)

home = os.path.expanduser("~")
desktop = os.path.join(home,"Desktop")

source = os.path.join(desktop,"db")
dest = os.path.join(desktop,"db1")

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


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
        print(f"An Exception occured : [{e}]")

# def rename_selected(name=None,ext=None,source_dir=None,dest_dir=None):
#     try:
#         source_dir = Path(source_path)
#         dest_dir = Path(dest_dir)

#         if check_fd_status(source_dir):
#             if check_fd_status(source_path):
#                 if source_path.parent != dest_path.parent:
#                     raise Exception("[Source/Destination] must have the Same Parent [Path/Directory]")
#                 else:
#                     if os.path.isdir(source_dir):
#                         for root,dirs,files in os.walk(source_dir):
#                             for file in files:
#                                 if file.endswith(ext) and name in file:
#                                     source_path = os.path.join(root,file)
#                                     relative_path = os.path.relpath(source_path, source_dir)
#                                     dest_path = os.path.join(dest_dir,relative_path)
#                                     shutil.move(source_path,dest_path)
#                                     logger.info(f"Renamed Selected File :[{source_path}] to Destination : [{dest_path}]")
#     except Exception as e:
#         print(f"An Exception occured : [{e}]")


def rename_selected(name=None, ext=None, source_dir=None, prefix="", feat=None, start=1, width=3):
    try:
        counter = start
        if feat == "sub":
            for root, dirs, files in os.walk(source_dir):
                for file in sorted(files):
                    if not file.endswith(ext) and not name in file:
                        continue
                    else:
                        old_path = os.path.join(root, file)
                        stem, suffix = os.path.splitext(file)
                        new_name = f"{prefix}{counter:0{width}d}{suffix}"
                        new_path = os.path.join(root, new_name)

                        os.rename(old_path, new_path)
                        logger.info(f"Renamed [{old_path}] -> [{new_path}]")

                        counter += 1

        elif feat=="top":
            for file in sorted(os.listdir(source_dir)):
                if not file.endswith(ext) and not name in file:
                    continue
                else:
                    old_path = os.path.join(source_dir,file)
                    stem, suffix = os.path.splitext(file)
                    new_name = f"{prefix}{counter:0{width}d}{suffix}"
                    new_path = os.path.join(source_dir, new_name)
                    
                    os.rename(old_path, new_path)
                    logger.info(f"Renamed [{old_path}] -> [{new_path}]")

                    counter += 1
        else:
            logger.warning("function [rename_selected(feat=None)]")
            raise Exception("rename_selected() - (feat=None) 0 feature in use")
        
    except Exception as e:
        print()
        print(f"An Exception occured : [{e}]")
    

def rename_main():
    while True:
        clear_screen()
        render_screen_rename()

        user_input = input("""
        OPT Input : """)
        print()

        if user_input not in ['0','1','2']:
            print("Invalid Option")
                    
        if user_input == "0":
            clear_screen()
            loading_animation("Exiting Rename...", 3)
            break

        elif user_input == "1":
            source = input("Source Path (File/Dir) : ")
            dest = input("Source Path (File/Dir) + New Name : ")
            rename(source,dest)

        elif user_input == '2':
            try:
                feat = input("""
    [1] Top Level (Ignore Sub Dir(s))
    [2] Sub Level (Entire Sub Dir(s)Tree) 
            
            OPT Input : """)
                if feat == "1":
                    name = input("File Name : ")
                    ext = input("File Extension : ")
                    source = input("Source Path(Dir) : ")
                    prefix = input("Prefix(beginning word of file) : ")
                    rename_selected(name,ext,source,prefix,"top")

                elif feat == "2":
                    name = input("File Name : ")
                    ext = input("File Extension : ")
                    source = input("Source Path(Dir) : ")
                    prefix = input("Prefix(beginning word of file) : ")
                    rename_selected(name,ext,source,prefix,"sub")

                else:
                    logger.warning("function [rename_selected(feat=None)]")
                    raise Exception("rename_selected() - (feat=None) 0 feature in use")
                
            except Exception as e:
                print()
                print(f"An Exception occured : [{e}]")

        print()
        input("Press Enter to Continue...")