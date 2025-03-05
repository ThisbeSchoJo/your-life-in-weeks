# lib/cli.py

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

    print("Welcome to Your Life in Weeks!")
    while True:
        
        menu()
        
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "1":
            interact_with_weeks_data()
        elif choice == "2":
            interact_with_users_data()
        elif choice == "3":
            create_user()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with weeks data")
    print("2. Interact with users data")
    print("3. Create a new user")


if __name__ == "__main__":
    main()
