from api import weather_main, setup_logger
from api import render_screen_weather
import platform
import os

logger = setup_logger(__name__)

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def main():
    while True:
        clear_screen()
        render_screen_weather()

        user_input = input("""

            OPT Input : """)
        print()

        if user_input == "1":
            logger.info("...Starting Weather...")
            print()
            weather_main()

main()