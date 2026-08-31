from commands import copy,move,trash,rename,process_directory
from organize_util import check_f_status,check_d_status,check_fd_status,setup_logger,patterns,parser,formatter
import os

def main():
    while True:
        user_input = input("""
    [1] Copy File/Dir(Tree)
    [2] Move File/Dirs
    [3] Rename
    [4] Send2Trash
    [5] Parse_series
                
                OPT Input :""")
        if user_input not in ['1','2','3','4','5']:
            print("Invalid Option")
            
        if user_input == "0":
            exit()
        
        elif user_input == "1":
             copy_input = input("""
             [1] Files
             [2] Dir
             OPT Input : """)
             if copy_input == "1":
                 source = input("Source Path(File) : ")
                 dest = input("Destination Path : ")
                 copy("file",source,dest)
             elif copy_input == "2":
                source = input("Source Path(Dir) : ")
                dest = input("Destination Path : ")
                copy("dir",None,None,source,dest)
             else:
                 pass
        
        elif user_input == "2":
            move_input = input("""
             [1] Files
             [2] Dir
             OPT Input : """)
            if move_input == "1":
                source = input("Source Path (File) : ")
                dest = input("Destination Path : ")
                move("file",source,dest)
        
            elif move_input == "2":
                source = input("Source Path (Dir) : ")
                dest = input("Destination Path : ")
                move("dir",None,None,source,dest)
            
            else:
                pass
        
        elif user_input == "3":
            source = input("Source Path (File/Dir) : ")
            dest = input("Source Path (File/Dir) + New Name : ")
            rename(source,dest)
        
        elif user_input == "4":
            path = input("File/Dir Path : ")
            trash(path)
            
        elif user_input == "5":
            p_input = input("OPT Dir name : ")
            process_directory(p_input)
        
        print()
        input("Press Enter to Continue : ")
        
main()