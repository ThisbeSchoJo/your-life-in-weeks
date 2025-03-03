# lib/helpers.py
from models.week import Week
from models.user import User
from models.comment import Comment


def interact_with_weeks_data():
    while True:
        week_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_weeks()
        # elif choice == "2":
        #     interact_with_comments_data()
        else:
            print("Invalid choice")

def get_all_weeks():
    Week.get_all()

    print("Here is the data for all weeks:\n")

    for week in Week.all:
        print(week)

    input("\n--Enter any key to continue... --\n")

def interact_with_users_data():
    while True:
        comment_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_users()
        # elif choice == "2":
        #     interact_with_comments_data()
        else:
            print("Invalid choice")

def get_all_users():
    User.get_all()

    print("Here is the data for all users:\n")

    for user in User.all:
        print(user)

    input("\n--Enter any key to continue... --\n")

def exit_program():
    print("Goodbye!")
    exit()

def week_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Retrieve all weeks")
    # print("2. Interact with comments data")

def user_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Retrieve all users")
    # print("2. Interact with comments data")

