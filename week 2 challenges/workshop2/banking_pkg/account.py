
"""
# Mathias Adikpon
# File: workshop2/account.py
# 06/28/2025
"""

def  show_balance(balance):
    """Display the current balance of the account."""
    print(f"Current balance: ${0 if balance == 0 else f'{balance:.2f}'}")

 


def deposit(balance):
    """Deposit money into the account."""
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
        else:
            print("Invalid deposit amount.")
        return balance
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return balance


def withdraw(balance):
    """Withdraw money from the account."""
    try:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")
        return balance
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return balance


def logout(name):
    """Logout the user."""
    print(f"Goodbye {name}!")
