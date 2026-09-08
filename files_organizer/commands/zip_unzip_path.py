import shutil
import os
from organize_util import check_fd_status
from organize_util import setup_logger
import platform
from zipfile import ZipFile
import zipfile
from organize_util import loading_animation, render_screen_zip

logger = setup_logger(__name__)

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def zip_file(zip_name, source_file):
    try:
        if check_fd_status(source_file):
            print()
            if os.path.isfile(source_file):
                with ZipFile(zip_name,"w",compression=zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(source_file)
                    logger.info(f"Added to Zip...Path :[{os.path.abspath(source_file)}]")
            else:
                logger.info(f"Source file [{source_file}] does not exist./ Not a valid file path.")

    except Exception as e:
        print(f"An Exception occured : [{e}]")

def zip_selected(zip_name=None,name=None,ext=None,source_dir=None):
    try:
        if check_fd_status(source_dir):
            print()
            if os.path.isdir(source_dir):
                with ZipFile(zip_name,"w",compression=zipfile.ZIP_DEFLATED) as zipf:
                    success = False
                    for root,dirs,files in os.walk(source_dir):
                        for file in files:
                            if file.endswith(ext) and name in file:
                                source_path = os.path.join(root,file)
                                zipf.write(source_path)
                                success = True
                                logger.info(f"Added to Zip...Path :[{os.path.abspath(source_path)}]")
                    if not success:
                        logger.info(f"No files found with name [{name}] and extension [{ext}] in directory [{source_dir}]")
                
    except Exception as e:
        print(f"An Exception occured : [{e}]")

def unzip_path(zip_name=None,dest_dir=None):
    try:
        if zipfile.is_zipfile(zip_name):
            with ZipFile(zip_name,"r") as zipf:
                if dest_dir is None:
                    zipf.extractall()
                    logger.info(f"Extracted Zip...Path :[{os.path.abspath(zip_name)}] to [{os.path.abspath(dest_dir)}]")
                else:
                    zipf.extractall(dest_dir)
                    logger.info(f"Extracted Zip...Path :[{os.path.abspath(zip_name)}] to [{os.path.abspath(dest_dir)}]")
    except Exception as e:
        print(f"An Exception occured : [{e}]")


def zip_main():
    while True:
        clear_screen()
        render_screen_zip()
        user_input = input("""
        OPT Input : """)
        print()

        if user_input not in ['0','1','2','3']:
            logger.info("Invalid Option Selected")

        if user_input == "0":
            clear_screen()
            loading_animation("Exiting Zip/Unzip...", 1)
            break

        elif user_input == "1":
            zip = input("Enter Zip File Name (with .zip extension) : ")
            name = input("Enter Source File Name (with extension) : ")
            print()
            zip_file(zip,name)

        elif user_input == "2":
            zip = input("Enter Zip File Name (with .zip extension) : ")
            name = input("Enter Source File Name (without extension) : ")
            ext = input("Enter Source File Extension (with .) : ")
            source_dir = input("Enter Source Directory Path : ")
            print()
            zip_selected(zip,name,ext,source_dir)

        elif user_input == "3":
            zip = input("Enter Zip file Path (with .zip extension) : ")
            dest_dir = input("Enter Destination Directory Path (Leave Blank for Current Directory) : ")
            print()
            unzip_path(zip,dest_dir)

        print()
        input("Press Enter to Continue...")

            

