# lib/cli.py

from helpers import (
    exit_program,
    interact_with_weeks_data,
    interact_with_users_data
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            interact_with_weeks_data()
        elif choice == "2":
            interact_with_users_data()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with weeks data")
    print("2. Interact with users data")


if __name__ == "__main__":
    main()
