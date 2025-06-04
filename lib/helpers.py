# lib/helpers.py
from models.week import Week
from models.user import User
from PIL import Image
from rich.console import Console

console = Console()
def interact_with_weeks_data():
    while True:
        week_menu()
        choice = input("> ")
        if choice == "1":
            get_all_weeks()
        elif choice == "2":
            get_weeks_by_satisfaction()
        elif choice == "3":
            get_weeks_by_user()
        elif choice == "4":
            delete_week()
        elif choice == "5":
            return  # Return to main menu
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice")

def get_all_weeks():
    weeks = Week.get_all()

    print("Here is the data for all weeks:\n")

    for week in weeks:
        user = User.find_by_id(week.user_id)
        print(f"Week ID: {week.id}, User: {user.name if user else 'Unknown'}, Date: {week.date}, Rating: {week.satisfaction_rating}, Summary: {week.comments}")

    console.input("[black]--Press any key to continue...--[/black]")

def get_weeks_by_satisfaction():
    print("\nEnter the minimum satisfaction rating for weeks displayed.\n")
    min_rating  = input("> ")
    try:
        min_rating = int(min_rating)
    except ValueError:
        print("Please enter a valid integer for the minimum rating.")
        return
    Week.filter_weeks_by_satisfaction(min_rating)
    console.input("[black]--Press any key to continue...--[/black]")

def get_weeks_by_user():
    User.get_all()
    print("Here is the data for all users:\n")
    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")
    print("\nEnter the user id for the user whose weeks you would like to display.\n")
    selected_user_id  = input("> ")
    try:
        selected_user_id = int(selected_user_id)
    except ValueError:
        print("Error: Please enter a valid integer for the user ID.")
        return
    Week.filter_weeks_by_user(selected_user_id)
    console.input("[black]--Press any key to continue...--[/black]")

def delete_week():
    Week.get_all()
    print("Here is the data for all weeks:\n")
    for week in Week.all:
        user = User.find_by_id(week.user_id)
        print(f"Week ID: {week.id}, User: {user.name if user else 'Unknown'}, Date: {week.date}, Rating: {week.satisfaction_rating}, Summary: {week.comments}")
    week_id = input("Enter the ID of the week to delete: ")
    week = Week.find_by_id(week_id)

    if week:
        confirm = input(f"Are you sure you want to delete Week {week.id}? (y/n): ").lower()
        if confirm == "y":
            week.delete()  # Calls the delete method from the Week class
            print(f"Week {week.id} has been deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Week not found.")

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
            delete_user()
        elif choice == "5":
            return  # Return to main menu
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice")

def get_all_users():
    User.get_all()

    print("Here is the data for all users:\n")

    for user in User.all:
        print(f"User ID: {user.id}, Name: {user.name}, Birthdate: {user.birthdate}")

    console.input("[black]--Press any key to continue...--[/black]")

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

    console.input("[black]--Press any key to continue...--[/black]")

    console.print("[italic cyan]Sometimes life seems really short, and other times it seems impossibly long.\n[italic cyan]")
    console.print("[italic cyan]But this chart is meant to emphasize that it's certainly finite.\n[italic cyan]")
    console.print("[italic cyan]Those weeks are all you have.\n[italic cyan]")
    console.print("[italic cyan]Given that fact, the only appropriate word to describe your weeks is precious.[italic cyan]")

    console.input("[black]--Press any key to continue...--[/black]")

def create_user():
    name = input("Enter name: ")
    birthdate = input("Enter birthdate (YYYY-MM-DD): ")
    try:
        user = User.create(name, birthdate)
        print(f"User {user.name} created successfully with ID {user.id}")
    except:
        raise Exception(f"Error creating User {user.name}!")
    
def delete_user():
    user_id = input("Enter the ID of the user to delete: ")
    user = User.find_by_id(user_id)

    if user:
        confirm = input(f"Are you sure you want to delete User {user.id}? (y/n): ").lower()
        if confirm == "y":
            user.delete()  # Calls the delete method from the Week class
            print(f"User {user.id} has been deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("User not found.")


def exit_program():

    console.print("[italic bold cyan]\nThere are trillions upon trillions of weeks in eternity, and this grid is your tiny handful.\n[italic bold cyan]")
    console.print("[italic bold cyan]Imagine each of your weeks is a small, .05 carat diamond.\n[italic bold cyan]")
    console.print("[italic bold cyan]If you multiply the volume of a .05 carat diamond by the number of weeks in 90 years (4,680), it adds up to just under a tablespoon.\n[italic bold cyan]")
    console.print("[italic bold cyan]Are you making the most of your weeks?\n[italic bold cyan]")
    console.input("[black]--Press any key to continue...--[/black]")
    img = Image.open("lib/diamond_spoon.png")  
    img.show()  # Opens with the system's default image viewer

    exit()

def week_menu():
    print("Please select an option:")
    print("1. Retrieve all weeks")
    print("2. Retrieve weeks based on satisfaction rating")
    print("3. Retrieve weeks for a specific user")
    print("4. Delete a week")
    print("5. Return to main menu")
    print("6. Exit the program")

def user_menu():
    print("Please select an option:")
    print("1. Retrieve all users")
    print("2. Select user to see their life in weeks")
    print("3. Create a new user")
    print("4. Delete a user")
    print("5. Return to main menu")
    print("6. Exit the program")

