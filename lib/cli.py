# lib/cli.py
# from colorama import Fore, Style
from rich.console import Console

from helpers import (
    exit_program,
    interact_with_weeks_data,
    interact_with_users_data,
    create_user
)
from models.user import User
from models.week import Week


def main():
    User.create_table()
    Week.create_table()
    console = Console()

    # print(Style.BRIGHT + Fore.GREEN + "\nWelcome to Your Life in Weeks!\n" + Style.RESET_ALL)
    console.print("[bold cyan]\nWelcome to Your Life in Weeks![/bold cyan]\n")
    console.print("[italic cyan]It kind of feels like our lives are made up of a countless number of weeks.[italic cyan]\n")
    console.print("[italic cyan]We imagine we will walk our dogs a hundred more times, we agonize over something embarrassing we said, \nwe pull our hair out over our crying toddler, we tell ourselves we'll finally ask out the barista next time, \nwe forget to return our sister's phone call, our plans never make it out of the friend's group chat, \nwe make shallow small talk and forget to listen when others respond, we tell ourselves we will go skydiving *someday*, \nwe hold off saying 'I love you' because it is too soon, we get annoyed with our mother's nagging, \nwe think 'how's work?' is enough with our father, we stay at a job that makes us miserable for fear of change. [italic cyan]\n")
    console.print("[italic cyan]We let a million moments pass us by unnoticed, unappreciated, or untouched, because we think we have unlimited time.[italic cyan]\n")
    console.print("[italic cyan]A passing week feels like a drop in the bucket of our time. [italic cyan]\n")
    console.print("[italic cyan]But truly, we each only get a finite, countable number of weeks... [italic cyan]\n\n")
    console.print("[italic cyan]This interactive CLI tool lays out your life before you—every week you've lived and every week you have left.[italic cyan]\n")
    while True:
        
        menu()

        choice = input("> ")

        # if choice == "0":
        #     exit_program()
        if choice == "1":
            interact_with_weeks_data()
        elif choice == "2":
            interact_with_users_data()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    # print("0. Exit the program")
    print("1. Interact with weeks data")
    print("2. Interact with users data")
    print("3. Exit the program")

if __name__ == "__main__":
    main()
