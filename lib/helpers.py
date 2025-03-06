# lib/helpers.py
from models.week import Week
from models.user import User
from PIL import Image

def interact_with_weeks_data():
    while True:
        week_menu()
        choice = input("> ")
        # if choice == "0":
        #     exit_program()
        if choice == "1":
            get_all_weeks()
        elif choice == "2":
            get_weeks_by_satisfaction()
        elif choice == "3":
            get_weeks_by_user()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")

def get_all_weeks():
    weeks = Week.get_all()

    print("Here is the data for all weeks:\n")

    for week in weeks:
        user = User.find_by_id(week.user_id)
        print(f"Week ID: {week.id}, User: {user.name if user else 'Unknown'}, Date: {week.date}, Rating: {week.satisfaction_rating}, Summary: {week.comments}")

    input("\n--Enter any key to continue... --\n")

def get_weeks_by_satisfaction():
    print("\nEnter the minimum satisfaction rating for weeks displayed.\n")
    min_rating  = input("> ")
    Week.filter_weeks_by_satisfaction(min_rating)

    input("\n--Enter any key to continue... --\n")

def get_weeks_by_user():
    print("\nEnter the user id for the user whose weeks you would like to display.\n")
    selected_user_id  = input("> ")
    try:
        selected_user_id = int(selected_user_id)
    except ValueError:
        print("Error: Please enter a valid integer for the user ID.")
        return
    # print(selected_user_id)
    Week.filter_weeks_by_user(selected_user_id)

    input("\n--Enter any key to continue... --\n")

def interact_with_users_data():
    while True:
        user_menu()
        choice = input("> ")
        if choice == "1":
            get_all_users()
        elif choice == "2":
            select_user_to_see_life_in_weeks()
        elif choice == "3":
            create_user()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")

def get_all_users():
    User.get_all()

    print("Here is the data for all users:\n")

    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")

    input("\n--Enter any key to continue... --\n")

def select_user_to_see_life_in_weeks():
    User.get_all()
    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")
    print("\nPlease enter the id of a user whose life you would like to see in weeks.\n")
    selected_user_id = input("> ")
    selected_user = User.find_by_id(selected_user_id)
    print(f"{selected_user.name}'s life in weeks:")
    if selected_user:
        selected_user.print_life_in_weeks()
    else:
        print("User not found")
    # User.find_by_id(selected_user_id)
    # User.print_life_in_weeks(selected_user_id)
    input("\n--Enter any key to continue... --\n")

def create_user():
    name = input("Enter name: ")
    birthdate = input("Enter birthdate (YYYY-MM-DD): ")
    try:
        user = User.create(name, birthdate)
        print(f"User {user.name} created successfully with ID {user.id}")
    except:
        raise Exception(f"Error creating User {user.name}!")
    
def exit_program():
    print("Life is precious. Collect your diamonds wisely.")
    img = Image.open("lib/diamond_spoon.png")  
    img.show()  # Opens with the system’s default image viewer

    exit()

def week_menu():
    print("Please select an option:")
    # print("0. Exit the program")
    print("1. Retrieve all weeks")
    print("2. Retrieve weeks based on satisfaction rating")
    print("3. Retrieve weeks for a specific user")
    print("4. Exit the program")
    # print("2. Interact with comments data")

def user_menu():
    print("Please select an option:")
    # print("0. Exit the program")
    print("1. Retrieve all users")
    print("2. Select user to see their life in weeks")
    print("3. Create a new user")
    print("4. Exit the program")
    # print("2. Interact with comments data")

