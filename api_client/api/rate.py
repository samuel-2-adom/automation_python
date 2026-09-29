from .setup_logger import setup_logger
from .render_screen import render_screen_rate
import requests
import os
import platform
from dotenv import load_dotenv
load_dotenv()

logger = setup_logger(__name__)

exchangerate_api = os.environ["EXCHANGE_RATES_API_KEY"]
rest_api = os.environ["RESTCOUNTRIES_API_KEY"]

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def build(id,data,f_amount=None):
    if id == "exchange_rate":
        base_code = data.get("base_code")
        rates = data.get("conversion_rates")
        for i in rates:
            print(f"       1 [{base_code}] ----|---- {rates[i]} [{i}]")
            
    
    elif id == "exchange_c":
        rate = data.get("conversion_rate")
        result = data.get("conversion_result")
        
        print(data.get("base_code"),":",data.get("target_code"),sep="\t")
        print("---"*8)
        print("1.0",":",rate,sep="\t")
        print(" ---"*8)
        print(f_amount,":",result,sep="\t")
        print("---"*8)
        print()
    
    elif id == "rest_rate":
        object = data["data"].get("objects")[0]
        base = object["base"]
        rates = object["rates"]
        for i in rates:
            print(f"      1.0 [{base}] ----|---- [{i}] {rates[i]}")
    
    elif id == "rest_c":
        object = data["data"].get("objects")
        for i in object:
            print(i["from"]["code"],":",i["to"].get("code"),sep="\t")
            print("---"*8)
            print("1",":",f"{i["rate"]:.02f}",sep="\t")
            print("---"*8)
            print(i["amount"],":",f"{i["result"]:.02f}",sep="\t")
            print()
        
          
def get_rate_exchange():
    while True:
        base = input("    OPT in base_currency_code [USD] : ").upper()
        print()
        if not base:
            base = "USD"
            
        url = f"https://v6.exchangerate-api.com/v6/{exchangerate_api}/latest/{base}"
        response = requests.get(url)
        
        if response.status_code == 404:
            print()
            logger.error(f"...[{base}] is an Invalid Base Currency Code...")
            print()
            try_again = input("Try Again [y/N] : ").lower()
            if try_again in ("y","yes"):
                print()
                continue
            break
            
        build("exchange_rate",response.json())

        print()
        input("  OPT in Enter to continue : ")
        break

def get_rate_exchange_c():
    while True:
        try:
            print()
            from_base = input("From Base Currency [GHS]: ").upper()
            print()
            if not from_base:
                from_base = "GHS"
            to = input("To Curency [USD]: ").upper()
            print()
            if not to:
                to = "USD"
            amount = float(input("Amount : "))
            print()
            
            url = f"https://v6.exchangerate-api.com/v6/{exchangerate_api}/pair/{from_base}/{to}/{amount}"
        
            response = requests.get(url)
            
            if response.status_code == 404:
                print()
                logger.error(f"...[{from_base}/{to}] is an Invalid Base Currency Code...")
                print()
                try_again = input("Try Again [y/N] : ").lower()
                if try_again in ("y","yes"):
                    print()
                    continue
                break
               
            build("exchange_c", response.json(),amount)

            input("    OPT in Enter to continue : ")
            break
                
        except ValueError:
            print()
            logger.info("Invalid Conversion Amount!!!!")
            print()

def get_rate_rest():
    while True:
        base = input("    OPT in base_currency_code [USD] : ").upper()
        print()
        if not base:
            base = "USD"
        url = "https://api.restcountries.com/currencies/v1/rates"
        headers = {"Authorization" : f"Bearer {rest_api}" }
        params = {"base" : base}
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 400:
            print()
            logger.error(f"...[{base}] is an Invalid Base Currency Code...")
            print()
            try_again = input("Try Again [y/N] : ").lower()
            if try_again in ("y","yes"):
                print()
                continue
            break
        
        response.raise_for_status()

        data = response.json()

        build("rest_rate",data)

        input("  OPT in Enter to continue : ")
        break

def get_rate_rest_c():
    while True:
        try:
            print()
            from_base = input("From Base Currency [GHS]: ").upper()
            print()
            if not from_base:
                from_base = "GHS"
            to = input("To Curency [USD]: ").upper()
            print()
            if not to:
                to = "USD"
            amount = float(input("Amount : "))
            print()

            url = "https://api.restcountries.com/currencies/v1/convert"
            headers = {"Authorization" : f"Bearer {rest_api}" }
            params = {"from" : from_base, "to" : to, "amount" : amount, "pretty" : 2}
            response = requests.get(url,params=params,headers=headers)

            if response.status_code == 400:
                logger.error(f"...[{from_base}/{to}] is an Invalid Base Currency Code...")
                print()
                try_again = input("Try Again [y/N] : ").lower()
                if try_again in ("y","yes"):
                    print()
                    continue
                break

            response.raise_for_status()

            data = response.json()

            build("rest_c",data)

            input("    OPT in Enter to continue : ")
            break

        except ValueError:
            print()
            logger.info("Invalid Conversion Amount!!!!")
            print()

def rate_main():
    while True:
        clear_screen()
        render_screen_rate("ExchangeRate Main")

        print()
        
        user_input = input("       OPT In : ")
        if user_input == "0":
            print()
            logger.info("Exiting ExchangeRate Main....")
            break

        elif user_input == "1":
            try:
                get_rate_rest()
            except requests.exceptions.HTTPError:
                print()
                logger.error(f"HTTPError - Switching API")
                print()
                get_rate_exchange()
            except requests.exceptions.RequestException as e:
                print(f"An exception Occured : [{e}]")

        elif user_input == "2":
            try:
                get_rate_rest_c()
            except requests.exceptions.HTTPError:
                print()
                logger.error(f"HTTPError - Switching API")
                print()
                get_rate_exchange_c()
            except requests.exceptions.RequestException as e:
                print(f"An exception Occured : [{e}]")

if __name__ == "__main__":
    try:
        rate_main()
    except requests.exceptions.RequestException as e:
        print(f"An exception occured : [{e}]")

