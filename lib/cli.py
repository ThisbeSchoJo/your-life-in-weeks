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

    print("\nWelcome to Your Life in Weeks!\n")
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
