# Your Life in Weeks


## Introduction

"Your Life in Weeks" is a Python-based Command Line Interface (CLI) application that visualizes a user's life as a grid of weeks, inspired by Tim Urban's blog post on mortality awareness. The app calculates the number of weeks lived and remaining based on the user's birthdate and assumed lifespan. It allows users to mark significant events, track life satisfaction, and visualize progress using an ASCII-based life calendar.


## Generating Your Environment

Clone the repository: 
    
    git clone https://github.com/ThisbeSchoJo/your-life-in-weeks

Navigate to the project directory:

    cd your-life-in-weeks

Install dependencies using Pipenv:

    pipenv install

Activate the virtual environment:

    pipenv shell

Run the application:

    python lib/cli.py

---


## Features:

User and Week Models:
- User Model: Represents an individual, storing their name, birthdate, and associated weeks. It includes methods for:
    1. Storing and retrieving user data.
    2. Calculating the number of weeks lived and the number of weeks left based on an assumed lifespan (80 years).
    3. Printing a visual representation of their life in weeks using emojis (⬜, 🟩, 💎) to denote weeks lived, weeks left, and weeks with data entries respectively.
- Week Model: Represents a specific week in a user's life, storing satisfaction ratings, comments, and the date of the week. It includes methods for:
    1. Storing and retrieving week data.
    2. Calculating the week number based on the user’s birthdate.
    3. Associating comments with weeks.
    4. Filtering weeks based on satisfaction rating.

Database Structure:
- The users table stores user data, while the weeks table stores week-specific data linked to a user via user_id.
- Methods for interacting with the database include creating, fetching, deleting, and updating user and week records.

CLI Interface:
- The CLI prompts the user with messages about the significance of life in weeks, encouraging reflection on their finite time.
- It offers an interactive experience, using the rich library to format colorful output and to handle user input.
- The main function sets up the tables for users and weeks, introduces the concept of "Your Life in Weeks," and waits for user interaction.


## CLI Flow:
The application begins by printing a welcome message, setting the stage for an emotional journey about the passage of time. After initial user input, it proceeds to allow the user to interact with the data. Here’s how the flow unfolds:

1. Introduction: The user is welcomed and provided with a philosophical message about life and time.
2. Data Interaction: The user can perform actions related to:
    - Viewing their weeks.
    - Logging satisfaction ratings and comments for each week
    - Viewing a visual representation of their life in weeks, where each week is shown using different emojis based on whether it’s lived, logged, or still ahead.


## Acknowledgements

Inspired by Tim Urban’s "Your Life in Weeks" concept and other mortality-awareness projects.