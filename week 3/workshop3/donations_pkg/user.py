"""
# workshop3.user
# This module contains functions for user login and registration.
# Mathias Adikpon
Juily, 5 2025
"""

def login(database, username, password):
    """Login a user by checking the username and password against the database."""
    # case-insensitive username : convert to lowercase and strip whitespace
    username = username.strip().lower() 
    if((username in database) and (database[username] == password)): # same as (database.get(username) == password)
        print(f"\nWelcome back {username.capitalize()}!")
        return username
    elif ((username in database) and (database[username] != password)): 
        print("\nIncorrect password. Please try again.")
        return ""
    else:
         # dynamic message with username
        print(f"\n{username.capitalize()} not found. Please register.")
        # print("User not found. Please register.") // static message
        return ""

def register(database, username, password):
    """Register a new user if the username is not already in the database."""
    # case-insensitive username : convert to lowercase and strip whitespace
    username = username.strip().lower()
    if not username: # Check if username is empty string
        print("\nUsername must have at least one character.")
        return ""
    elif not (username[0].isalpha() and username.isalnum()):
        print("\nUsername must start with a letter and contain only alphanumeric characters.")
        return ""
    elif len(username) > 10:
        print("\nUsername must not exceed 10 characters.")
        return ""
    elif not password: # Check if password is empty string
        print("\nPassword must have at least one character.")
        return ""
    elif len(password) < 5:
        print("\nPassword must be at least 5 characters long.")
        return ""
    elif username in database:
        print(f"\n{username.capitalize()} already registered.")
        return ""
    elif username[0].isalpha() and username.isalnum(): #This can also use else statement
        print(f"\n{username.capitalize()} has been registered successfully!")
        return username
    else:
        # Other invalid cases/ however, this should not be reached due to previous checks
        print("\nInvalid registeration. Please try again.")
        return ""