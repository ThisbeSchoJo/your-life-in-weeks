# lib/helpers.py
from models.week import Week
from models.user import User
from PIL import Image
# from models.comment import Comment


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

def create_user():
    name = input("Enter name: ")
    birthdate = input("Enter birthdate (YYYY-MM-DD): ")
    try:
        user = User.create(name, birthdate)
        print(f"User {user.name} created successfully with ID {user.id}")
    except:
        raise Exception(f"Error creating User {user.name}!")

def get_all_weeks():
    weeks = Week.get_all()

    print("Here is the data for all weeks:\n")

    for week in weeks:
        user = User.find_by_id(week.user_id)
        print(f"Week ID: {week.id}, User: {user.name if user else 'Unknown'}, Date: {week.date}, Rating: {week.satisfaction_rating}, Summary: {week.comments}")

    input("\n--Enter any key to continue... --\n")

def interact_with_users_data():
    while True:
        user_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_users()
        elif choice == "2":
            select_user_to_see_life_in_weeks()
        else:
            print("Invalid choice")

def get_all_users():
    User.get_all()

    print("Here is the data for all users:\n")

    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")

    input("\n--Enter any key to continue... --\n")

def select_user_to_see_life_in_weeks():
    # input to select user
    # call a function in User that will display that user's life in weeks
    User.get_all()
    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")
    print("\nPlease enter the id of a user whose life you would like to see in weeks.\n")
    selected_user_id = input("> ")
    selected_user = User.find_by_id(selected_user_id)
    print(f"{selected_user}'s life in weeks is loading...")
    if selected_user:
        selected_user.print_life_in_weeks()
    else:
        print("User not found")
    # User.find_by_id(selected_user_id)
    # User.print_life_in_weeks(selected_user_id)
    input("\n--Enter any key to continue... --\n")

def exit_program():
    print("Goodbye!")
    img = Image.open("lib/diamond_spoon.png")  
    img.show()  # Opens with the system’s default image viewer

    print("Life is precious. Collect your diamonds wisely.")
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
    print("2. Select user to see their life in weeks")
    # print("2. Interact with comments data")

