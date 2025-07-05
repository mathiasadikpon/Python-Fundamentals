
"""
# workshop3.user with class
# This module contains class for user login and registration.
# It includes methods for logging in and registering a new user with validation checks.
# Mathias Adikpon
Juily, 5 2025
"""
class User:
    def __init__(self, database= {"admin": "password123"}, username="", password=""):
        self.database = database
        self.username = username.strip().lower()  # case-insensitive username
        self.password = password
    
    def login(self):
        """Login a user by checking the username and password against the database."""
        if self.username in self.database and self.database[self.username] == self.password:
            print(f"\nWelcome back {self.username.capitalize()}!")
            return self.username
        elif self.username in self.database and self.database[self.username] != self.password:
            print("\nIncorrect password. Please try again.")
            return ""
        else:
            print(f"\n{self.username.capitalize()} not found. Please register.")
            return ""
    
    def register(self):
        """Register a new user if the username is not already in the database."""
        if not self.username:  # Check if username is empty string
            print("\nUsername must have at least one character.")
            return ""
        elif not (self.username[0].isalpha() and self.username.isalnum()):
            print("\nUsername must start with a letter and contain only alphanumeric characters.")
            return ""
        elif len(self.username) > 10:
            print("\nUsername must not exceed 10 characters.")
            return ""
        elif not self.password:  # Check if password is empty string
            print("\nPassword must have at least one character.")
            return ""
        elif len(self.password) < 5:
            print("\nPassword must be at least 5 characters long.")
            return ""
        elif self.username in self.database:
            print(f"\n{self.username.capitalize()} already registered.")
            return ""
        elif self.username[0].isalpha() and self.username.isalnum():  # This can also use else statement
            print(f"\n{self.username.capitalize()} has been registered successfully!")
            return self.username
        else:
            # Other invalid cases/ however, this should not be reached due to previous checks
            print("\nInvalid registration. Please try again.")
            return ""
    

    
