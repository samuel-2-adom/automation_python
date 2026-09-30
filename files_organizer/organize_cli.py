from commands import copy,move,trash,rename,process_directory,copy_main,move_main,trash_main,rename_main,process_directory_main,zip_main
from organize_util import check_f_status,check_d_status,check_fd_status,setup_logger,patterns,parser,formatter
from organize_util import loading_animation, render_screen_main
import os
import platform

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def main():
    loading_animation(2)  # Show loading animation for 2 seconds
    while True:
        clear_screen()
        render_screen_main()

        user_input = input("""
    OPT Input : """)
        print()

        if user_input not in ("0","1","2","3","4","5","6"):
            print("Invalid Option Selected....")

        if user_input == "0":
            print("🚀🚀🚀 GoodBye Exiting Organizer....")
            print()
            exit()

        elif user_input == "1":
            copy_main()

        elif user_input == "2":
            move_main()

        elif user_input == "3":
            rename_main()

        elif user_input == "4":
            trash_main()

        elif user_input == "5":
            process_directory_main()

        elif user_input == "6":
            zip_main()

        print()
        input("Press Enter to Continue...")
        
if __name__ == "__main__":      
    main()