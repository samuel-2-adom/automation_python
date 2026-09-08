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
        
        
main()

#def main():
    # while True:
    #     user_input = input("""
    # [1] Copy File/Dir(Tree)
    # [2] Move File/Dirs
    # [3] Rename
    # [4] Send2Trash
    # [5] Parse_series
                
    #             OPT Input :""")
    #     if user_input not in ['1','2','3','4','5']:
    #         print("Invalid Option")
            
    #     if user_input == "0":
    #         exit()
        
    #     elif user_input == "1":
    #          copy_input = input("""
    #          [1] Files
    #          [2] Dir
    #          OPT Input : """)
    #          if copy_input == "1":
    #              source = input("Source Path(File) : ")
    #              dest = input("Destination Path : ")
    #              copy("file",source,dest)
    #          elif copy_input == "2":
    #             source = input("Source Path(Dir) : ")
    #             dest = input("Destination Path : ")
    #             copy("dir",None,None,source,dest)
    #          else:
    #              pass
        
    #     elif user_input == "2":
    #         move_input = input("""
    #          [1] Files
    #          [2] Dir
    #          OPT Input : """)
    #         if move_input == "1":
    #             source = input("Source Path (File) : ")
    #             dest = input("Destination Path : ")
    #             move("file",source,dest)
        
    #         elif move_input == "2":
    #             source = input("Source Path (Dir) : ")
    #             dest = input("Destination Path : ")
    #             move("dir",None,None,source,dest)
            
    #         else:
    #             pass
        
    #     elif user_input == "3":
    #         source = input("Source Path (File/Dir) : ")
    #         dest = input("Source Path (File/Dir) + New Name : ")
    #         rename(source,dest)
        
    #     elif user_input == "4":
    #         path = input("File/Dir Path : ")
    #         trash(path)
            
    #     elif user_input == "5":
    #         p_input = input("OPT Dir name : ")
    #         process_directory(p_input)
        
    #     print()
    #     input("Press Enter to Continue : ")

#main()