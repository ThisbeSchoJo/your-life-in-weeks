# lib/helpers.py
from models.week import Week
from models.comment import Comment


def interact_with_weeks_data():
    while True:
        week_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            interact_with_weeks_data()
        elif choice == "2":
            interact_with_comments_data()
        else:
            print("Invalid choice")
    print("Interacting with weeks data...")
    input("--Enter any key to continue... --")

def interact_with_comments_data():
    while True:
        comment_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            interact_with_weeks_data()
        elif choice == "2":
            interact_with_comments_data()
        else:
            print("Invalid choice")
    print("Interacting with comments data...")
    input("--Enter any key to continue... --")


def exit_program():
    print("Goodbye!")
    exit()

def week_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with weeks data")
    print("2. Interact with comments data")

def comment_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with weeks data")
    print("2. Interact with comments data")

