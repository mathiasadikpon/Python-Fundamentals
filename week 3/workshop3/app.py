"""
# workshop3.app
# Mathias Adikpon
Juily, 5 2025
"""

# Import necessary functions
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


# Declare variables
database = {"admin": "password123"}  
donations = []
authorized_user = ""

# Call the homepage function
show_homepage()

# User login 
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")


# Handle user options
# Loop until the user chooses to exit
while True:
    user_input = input("Choose an option: ").strip().lower()

    if user_input in ["1", "login"]:
        # User login functionality
        username = input("\nEnter your username: ").strip()
        password = input("Enter your password: ").strip()

        # Call the login function
        authorized_user = login(database, username, password)
        
    elif user_input in ["2", "register"]:
        # User registration functionality
        username = input("\nEnter your username: ").strip().lower()
        password = input("Enter your password: ").strip()

        # Call the register function
        authorized_user = register(database, username, password)
        if authorized_user:
            database[authorized_user] = password

    elif user_input in ["3", "donate"]:
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            # Donation functionality
            donation_string = donate(authorized_user)
            if donation_string != "":
                # Add donation when not empty
                donations.append(donation_string)
            
    elif user_input in ["4", "show donations"]:
        # Show all donations if any
        show_donations(donations)
    elif user_input in ["5", "exit"]:
        print("Leaving DonateMe...")
        break
    else:
        # Invalid input handling
        print("Invalid choice. Please try again.")
    
    # Show the homepage again
    show_homepage()
    # User login 
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user.capitalize()}")

# Task 6 need to be done:
# I push wrong comment