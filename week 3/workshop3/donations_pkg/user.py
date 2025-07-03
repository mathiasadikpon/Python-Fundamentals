"""
# workshop3.user
# This module contains functions for user login and registration.
# Mathias Adikpon
Juily, 5 2025
"""

def login(database, username, password):
    """Login a user by checking the username and password against the database."""
    if((username in database) and (database[username] == password)): # same as (database.get(username) == password)
        print(f"\nWelcome back {username}!")
        return username
    elif ((username in database) and (database[username] != password)): 
        print("\nIncorrect password. Please try again.")
        return ""
    else:
         # dynamic message with username
        print(f"\n{username} not found. Please register.")
        # print("User not found. Please register.") // static message
        return ""

def register(database, username):
    """Register a new user if the username is not already in the database."""
    if username in database:
        print(f"\n{username.capitalize()} already registered.")
        return ""
    else:
        print(f"\n{username.capitalize()} has been registered successfully!")
        return username