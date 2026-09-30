from .setup_logger import setup_logger
from .render_screen import render_screen_github
import os
import platform
import requests
import json
from dotenv import load_dotenv

load_dotenv()

logger = setup_logger(__name__)

github_token = os.environ["GITHUB_TOKEN"]

base = "https://api.github.com"


def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def build(id, data):
    if id == "user_repo":
        print()
        length = len(data)
        print("📊" + "─" * 10 + f" Total Public Repos: {length} " + "─" * 10)
        print()

        print("📁 Repository list")
        print("─" * 80)
        for i in data:
            print(f"📦 {i['name']}  →  🔗 {i['html_url']}")
            print()
        print("─" * 80)
        print()

    if id == "search":
        print(f"🔎 Total Repositories : [{data['total_count']}]")
        items = data["items"]
        for i in items:
            topics = ", ".join(i.get("topics", [])) if i.get("topics") else "No topics"
            description = i.get("description") or "No description provided"
            language = i.get("language",[]) if i.get("language") else "No Language"
            print()
            print(f"Repo Name 📦: {i['full_name']}")
            print(f"Stars ⭐ : {i['stargazers_count']}")
            print(f"Language 🕵️: {language}")
            print(f"Topic 🏷️ : {topics}")
            print(f"Description 📝 : {description}")
            print(f"URL 🔗 : {i['html_url']}")
            print("*" * 30)
    
def get_user_repo():

    headers = {"Authorization": f"Bearer {github_token}", "User-Agent": "PythonProgram1", "Accept": "application/vnd.github+json"}

    while True:
        user_name = input("👤 Enter User_Name : ")

        user_repo = f"{base}/users/{user_name}/repos"

        response = requests.get(user_repo, headers=headers)

        data = response.json()

        if response.status_code == 404:
            print()
            logger.info("Repo Not Found....")
            print()
            try_again = input("🔁 Try Again [y/N] : ").lower()
            if try_again in ("y", "yes"):
                continue
            break

        response.raise_for_status()

        print()
        print("---" * 20)
        print(f"🔗 GitHub URL : https://github.com/{user_name}")
        print("---" * 20)
        build("user_repo", data)

        try_again = input("🔁 Try Again [y/N] : ").lower()
        if try_again in ("y", "yes"):
            continue
        print()
        break


def search_repo():
    while True:
        search = input("Search Qualifier 🔎 : ")

        sort = input("Sort [created_at] 📅 : ") or "created_at"
        order = input("Order [asc] ↕️ : ") or "asc"

        per_page_input = input("Per_Page [5] 📄 : ")
        try:
            per_page = int(per_page_input) if per_page_input else 5
        except ValueError:
            per_page = 5
        if per_page < 1 or per_page > 100:
            per_page = 5

        page_input = input("Pagination [1] 📖 : ")
        try:
            page = int(page_input) if page_input else 1
        except ValueError:
            page = 1
        if page < 1:
            page = 1

        print()

        headers = {"Authorization": f"Bearer {github_token}", "User-Agent": "PythonProgram1", "Accept": "application/vnd.github+json"}
        params = {"q": search, "sort": sort, "order": order, "per_page": per_page, "page": page}

        repos = f"{base}/search/repositories"

        response = requests.get(repos, headers=headers, params=params)

        data = response.json()

        response.raise_for_status()

        build("search", data)

        try_again = input("🔁 Try Again [y/N] : ").lower()
        if try_again in ("y", "yes"):
            continue
        print()
        break
        
def github_main():
    while True:
        clear_screen()
        render_screen_github("Github Main")

        print()
        user_input = input("    OPT In : ")

        if user_input not in ("0","1","2"):
            continue

        if user_input == "0":
            logger.info("Exiting Github Main...")
            print()
            input("Enter to continue.....")
            break

        elif user_input == "1":
            try:
                print()
                get_user_repo()
            except requests.exceptions.RequestException as e:
                print(f"An exception Occured : [{e}]")

        elif user_input == "2":
            try:
                print()
                search_repo()
            except requests.exceptions.RequestException as e:
                print(f"An exception Occured : [{e}]")

if __name__ == "__main__":
    github_main()


