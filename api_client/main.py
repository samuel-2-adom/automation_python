from api import weather_main, setup_logger, render_screen, rate_main
import platform
import os

logger = setup_logger(__name__)

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def main():
    while True:
        clear_screen()
        render_screen()

        user_input = input("""

            OPT Input : """)
        print()

        if user_input not in ("1","2","3"):
            continue
        
        if user_input == "1":
            print()
            weather_main()

        elif user_input == "2":
            print()
            rate_main()

        elif user_input == "3":
            print()
            logger.info(".....In Progress.....")

main()