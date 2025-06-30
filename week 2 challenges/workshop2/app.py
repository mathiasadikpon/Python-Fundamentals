"""
# Mathias Adikpon
# File: workshop2/app.py
# 06/28/2025
"""
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Initialize variables
name = ""
pin = ""
balance = 0
# Task 2
def register_user():
    """
      Register a new user with a name and PIN
    """
    global name, pin, balance
    print("    === Automated Teller Machine ===    ")
    name = get_name("Enter name to register: ")
    pin = get_pin()
    balance = 0
    print(f"{name} has been registered with a starting balance of ${0 if balance == 0 else f'{balance:.2f}'}")

def get_pin():
    """
      Get the user's PIN
    """
    while True:
        _pin = input("Enter a 4-digit PIN: ").strip()
        if _pin.isdigit() and len(_pin) == 4:
            return _pin
        else:
            print("Invalid PIN. Please enter a 4-digit number.")


def get_name(message=""):
    """
    Get the user's name. Must be 1–10 characters, only letters or letters with numbers (no pure numbers, no spaces).
    """
    while True:
        _name = input(message).strip()
        if (1 <= len(_name) <= 10) and (_name.isalpha() or (_name.isalnum() and not _name.isdigit())):
            return _name
        else:
            print("Invalid name. Please enter 1–10 characters (letters or letters with numbers only, no spaces).")


# Call the register_user function to register a user
register_user()

# end task 2

# Task 3
while True:
    """Task 3: Request the user's name and PIN for login
    """
    print("\n    === Automated Teller Machine ===    ")
    print("LOGIN")
    name_to_validate = get_name("Enter name: ")
    pin_to_validate = get_pin()
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print( "Invalid credentials!") 


while True:
    """
    Ask user to make a choice from the menu until they choose to logout
    """
    atm_menu(name)
    option = input("Choose an option: ").strip().lower()
    if option in ["1", "balance"]:
        account.show_balance(balance)
    elif option in ["2", "deposit"]:
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option in["3", "withdraw"]:
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option in ["4", "logout"]:
        account.logout(name)
        break
    else:
        print("Invalid option. Please try again.")
    