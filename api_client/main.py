from api import weather_main, setup_logger

logger = setup_logger(__name__)

user_input = input("""
[1] Current Weather / Forcast
[2] Excahange Rate
[3] Github

    OPT Input : """)

if user_input == "1":
    logger.info("...Starting Weather...")
    weather_main()
