# lib/cli.py
from rich.console import Console

from helpers import (
    exit_program,
    interact_with_weeks_data,
    interact_with_users_data
)
from models.user import User
from models.week import Week

console = Console()
def main():
    User.create_table()
    Week.create_table()

    console.print("[bold cyan]\nWelcome to Your Life in Weeks![/bold cyan]\n")
    console.input("[black]--Press any key to continue...--[/black]")
    console.print("[italic cyan]It kind of feels like our lives are made up of a countless number of weeks.[italic cyan]\n")
    console.print("[italic cyan]A million moments pass us by unnoticed, unappreciated, or untouched, because we think we have unlimited time.[italic cyan]\n")
    console.print("[italic cyan]Each passing week can feel like a drop in the bucket of our time. [italic cyan]\n")
    console.input("[black]--Press any key to continue...--[/black]")
    console.print("[italic cyan]But truly, we each only get a finite, countable number of weeks... [italic cyan]\n")
    console.input("[black]--Press any key to continue...--[/black]")
    console.print("[italic cyan]This interactive CLI tool lays out your life before you—every week you've lived and every week you have left.[italic cyan]\n")
    console.input("[black]--Press any key to continue...--[/black]")
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
    print("1. Check out weeks' data")
    print("2. Mess with users' data")
    print("3. Exit the program")

if __name__ == "__main__":
    main()
