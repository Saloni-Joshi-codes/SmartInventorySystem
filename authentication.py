from getpass import getpass
from colorama import Fore, Style, init

init(autoreset=True)

USERNAME = "admin"
PASSWORD = "admin123"

def login():
    print(Fore.CYAN + "=" * 45)
    print("      SMART INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)

    attempts = 3

    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == USERNAME and password == PASSWORD:
            print(Fore.GREEN + "\nLogin Successful!\n")
            return True
        else:
            attempts -= 1
            print(Fore.RED + f"Invalid Username or Password!")
            print(Fore.YELLOW + f"Attempts Remaining: {attempts}\n")

    print(Fore.RED + "Too many failed attempts.")
    print("Exiting Program...")
    return False