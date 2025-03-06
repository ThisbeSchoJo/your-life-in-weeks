# lib/cli.py
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

    console.print("[bold cyan]\nWelcome to Your Life in Weeks![/bold cyan]\n")
    input("\n--Enter any key to continue... --\n")
    console.print("[italic cyan]It kind of feels like our lives are made up of a countless number of weeks.[italic cyan]\n")
    # console.print("[italic cyan]We imagine we will walk our dogs a hundred more times, \nwe agonize over something embarrassing we said, \nwe tell ourselves we'll finally ask out the barista next time, \nwe forget to return our sister's phone call, \nour plans never make it out of the friend's group chat, \nwe make shallow small talk and forget to listen when others respond, \nwe tell ourselves we will go skydiving *someday*, \nwe hold off saying 'I love you' because it is too soon, \nwe get annoyed with our mother's nagging, \nwe think 'how's work?' is enough with our father, \nwe stay at a job that makes us miserable for fear of change. [italic cyan]\n")
    # input("\n--Enter any key to continue... --\n")
    console.print("[italic cyan]A million moments pass us by unnoticed, unappreciated, or untouched, because we think we have unlimited time.[italic cyan]\n")
    console.print("[italic cyan]Each passing week can feel like a drop in the bucket of our time. [italic cyan]\n")
    input("\n--Enter any key to continue... --\n")
    console.print("[italic cyan]But truly, we each only get a finite, countable number of weeks... [italic cyan]\n")
    input("\n--Enter any key to continue... --\n")
    console.print("[italic cyan]This interactive CLI tool lays out your life before you—every week you've lived and every week you have left.[italic cyan]\n")
    input("\n--Enter any key to continue... --\n")
    while True:
        
        menu()

        choice = input("> ")
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
    print("1. Interact with weeks data")
    print("2. Interact with users data")
    print("3. Exit the program")

if __name__ == "__main__":
    main()
