"""
Workshop 4: Classes and Objects
description: This workshop focuses on creating a User class and a BankUser class that inherits from User.
Author: Mathias Adikpon
Date: 07/12/2025
"""

# import os for clearing the console
from __future__ import annotations  # For type hinting self-referential types
import os # Clear the console for better readability


""" Helper functions"""
def is_valid_name(name):
    """Checks if the name is valid: type string, not empty,  not just whitespace, and has characters between 2 and 10 inclusive."""
    if not isinstance(name, str):
        print("Name must be a string.")
        return False
    elif not name.strip():
        print("Name cannot be empty or just whitespace.")
        return False
    elif not name.isalnum():
        print("Name must contain only alphanumeric characters.")
        return False
    elif not name[0].isalpha():
        print("Name must start with an alphabetic character.")
        return False
    elif len(name) < 2 or len(name) > 10:
        print("Name must be between 2 and 10 characters long.")
        return False
    else:
        return True

def is_valid_pin(pin):
    """Checks if the pin is valid: type int or str, a 4-digit number, and not negative."""
    try:
        pin = int(pin)
        if pin < 0:
            print("Pin cannot be negative.")
            return False
        elif len(str(pin)) != 4:
            print("Pin must be exactly 4 digits long.")
            return False
        else:
            return True
    except:
        print("Pin must contain only digits.")
        return False 

def is_valid_password(password):
    """Checks if the password is valid: type string, not empty, not just whitespace, and has at least 5 characters."""
    if not isinstance(password, str):
        print("Password must be a string.")
        return False
    elif not password.strip():
        print("Password cannot be empty or just whitespace.")
        return False
    elif len(password.strip()) < 5:
        print("Password must be at least 5 characters long.")
        return False
    elif not password.strip().isalnum():
        print("Password must contain only alphanumeric characters.")
        return False
    else:
        return True

def private_formatter(value: float | int):
    """Formats the value to 1 decimal place if it is a float, otherwise returns the whole number if it is an integer. all returns value as a string."""
    if value % 1 == 0:
        return f"{value:.0f}"
    else:
        return f"{value:.1f}"   

""" Classes and Objects"""
class User:
    """ User class represents a user with a name, pin, and password. It provides methods to change these attributes."""

    def __new__(cls, name, pin, password):
        """Ensures that the User object is created only if the parameters are valid."""
        if not (is_valid_name(name) and
                is_valid_pin(pin) and
                is_valid_password(password)):
            print(f"\nInvalid {cls.__name__} initialization parameters.  Please check the parameters.\n")
            return None
        return super().__new__(cls)

    def __init__(self, name, pin, password):
        """Initializes the User object with a name, pin, and password."""      
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        """Changes the name of the User object if the new name is valid"""
        if is_valid_name(new_name):
            self.name = new_name
    
    def change_pin(self, new_pin):
        """Changes the pin of the User object if the new pin is a 4-digit number"""
        if is_valid_pin(new_pin):            
            self.pin = new_pin
    
    def change_password(self, new_password):

        if is_valid_password(new_password):            
            self.password = new_password

class BankUser(User):
    """ BankUser class inherits from User class """
    
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False  # Indicates if the account is on hold

    def show_balance(self):
        """Prints the BankUser object's balance"""
        print(f"{self.name.capitalize()} has an account balance of: {self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraws the specified amount from the BankUser's balance"""
        if self.on_hold:
            print(f"{self.name.capitalize()}'s account is on hold. Cannot withdraw funds.")
            return
        if isinstance(amount, str):
            try:
                amount = float(amount)
            except ValueError:
                print(f"{self.name.capitalize()} cannot withdraw a non-numeric value: {amount:.2f}")
                return
        if not isinstance(amount, (int, float)):
            print(f"{self.name.capitalize()} cannot withdraw a non-numeric value: {amount}")
            return
        if amount < 0:
            print(f"{self.name.capitalize()} cannot withdraw a negative amount: {amount:.2f}")
        elif amount > self.balance:
            print(f"{self.name.capitalize()} cannot withdraw {amount:.2f}. Insufficient funds.")
        else:
            self.balance -= amount
            # print(f"{self.name.capitalize()} withdrew {amount:.1f}. New balance: {self.balance:.1f}")

    def deposit(self, amount):
        """Deposits the specified amount to the BankUser's balance"""
        if self.on_hold:
            print(f"{self.name.capitalize()}'s account is on hold. Cannot deposit funds.")
            return
        if isinstance(amount, str):
            try:
                amount = float(amount)
            except ValueError:
                print(f"{self.name.capitalize()} cannot deposit a non-numeric value: {amount}")
                return
        if not isinstance(amount, (int, float)):
            print(f"{self.name.capitalize()} cannot deposit a non-numeric value: {amount}")
            return
        if amount < 0:
            print(f"{self.name.capitalize()} cannot deposit a negative amount: {amount:.2f}")
        else:
            self.balance += amount
            # print(f"{self.name.capitalize()} deposited {amount:.1f}. New balance: {self.balance:.1f}")

    def transfer_money(self, amount, receiver: BankUser):
        """Transfers the specified amount to another BankUser's balance"""
        print()
        if self.on_hold:
            print(f"{self.name.capitalize()}'s account is on hold. Cannot transfer funds.")
            return False
        if isinstance(amount, str):
            try:
                amount = float(amount)
            except ValueError:
                print(f"{self.name.capitalize()} cannot transfer a non-numeric value: {amount}")
                return False
        if not isinstance(amount, (int, float)):
            print(f"{self.name.capitalize()} cannot transfer a non-numeric value: {amount}")
            return False
        if amount < 0:
            print(f"{self.name.capitalize()} cannot transfer a negative amount: {amount:.2f}")
            return False
        if amount == 0:
            print(f"{self.name.capitalize()} cannot transfer zero amount.")
            return False
        if amount > self.balance:
            print(f"{self.name.capitalize()} cannot transfer {amount:.2f}. Insufficient funds.")
            return False
        if not isinstance(receiver, BankUser):
            print(f"{self.name.capitalize()} cannot transfer money to a non-BankUser: {receiver}")
            return False
        if receiver.name == self.name: 
            #self transfer check not allowed
            print(f"{self.name.capitalize()} cannot transfer money to themselves.")
            return False
        
        # Print the transfer details
        print(f"You are transferring ${amount:.2f} to {receiver.name.capitalize()}")
        # Authenticate the pin of the sender: sender is "self"
        print("Authentication required")
        pin = input("Enter your PIN: ").strip()
        if pin.isdigit() and int(pin) == self.pin:
            print("Transfer authorized")
            print(f"Transferring ${amount:.2f} to {receiver.name.capitalize()}")
            self.withdraw(amount)
            receiver.deposit(amount)
            return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False        
          
    def request_money(self, amount: float, sender: BankUser):
        """Requests the specified amount from another BankUser's balance bse on User receiving's pin and vlalide password of user requesting the money"""

        print()
        if self.on_hold:
            # If the account is on hold, print a message and return False
            print(f"{self.name.capitalize()}'s account is on hold. Cannot request funds.")
            return False
        
        # Check if the amount is valid
        if isinstance(amount, str):
            try:
                amount = float(amount)
            except ValueError:
                print(f"{self.name.capitalize()} cannot request a non-numeric value: {amount}")
                return False
        # Check if the amount is negative, zero, or exceeds the sender's balance
        if not isinstance(amount, (int, float)):
            print(f"{self.name.capitalize()} cannot request a non-numeric value: {amount}")
            return False        
        if amount < 0:
            print(f"{self.name.capitalize()} cannot request a negative amount: {amount:.2f}")
            return False
        if amount == 0:
            print(f"{self.name.capitalize()} cannot request zero amount.")
            return False
        if amount > sender.balance:
            print(f"{self.name.capitalize()} cannot request {amount:.2f}. Insufficient funds in {sender.name.capitalize()}'s account.")
            return False
        if not isinstance(sender, BankUser):
            print(f"{self.name.capitalize()} cannot request money from a non-BankUser: {sender}")
            return False
        if sender.name.strip().lower() == self.name.strip().lower():
            # self transfer request not allowed
            print(f"{self.name.capitalize()} cannot request money from themselves.")
            return False
        
        # Print the request details
        print(f"You are requesting ${amount:.2f} from {sender.name.capitalize()}")
        # Authenticate the pin of the sender
        print("User authentication is required...")
        pin = input(f"Enter {sender.name.capitalize()}'s PIN: ").strip()
        if pin.isdigit() and int(pin) == sender.pin:
            # Authenticate the password of the receiver: receiver is "self"
            password = input(f"Enter your password: ").strip()
            if password == self.password:
                print("Request authorized")
                sender.withdraw(amount)
                self.deposit(amount)
                print(f"{sender.name.capitalize()} sent ${amount:.2f}")
                return True
            else:
                print("Invalid password. Transaction canceled.")
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            return False
            

""" all driver code"""
os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability

""" Driver Code for Task 1 """
# user "Bob" as the name, 1234 as the pin, and "password" as the password
user = User("Bob", 1234, "password")
print(f"{user.name} {user.pin} {user.password}")

""" Driver Code for Task 2 """
# change the name to "Bobby", pin to 4321, and password to "newpassword"
user.change_name("Bobby")
user.change_pin(4321)
user.change_password("newpassword")
print(f"{user.name} {user.pin} {user.password}")
print()

""" Driver Code for Task 3"""
# bankBob = BankUser("Bob", 1234, "password")
# print(f"{bankBob.name} {bankBob.pin} {bankBob.password} {bankBob.balance}")

""" Driver Code for Task 4"""
# #Instantiate an object of the BankUser class
# bankBob = BankUser("Bob", 1234, "password") 
# # Call the show_balance method to print the balance
# bankBob.show_balance()
# # deposit 1000 to the balance
# bankBob.deposit(1000)
# # Call the show_balance method to print the balance
# bankBob.show_balance()
# # withdraw 500 from the balance
# bankBob.withdraw(500)
# # Call the show_balance method to print the balance
# bankBob.show_balance()

""" Driver Code for Task 5"""
# Instantiate two objects of the BankUser class
bankBob = BankUser("Bob", 1234, "password") 
bankAlice = BankUser("Alice", 5678, "alicepassword")
# Deposit $5000 into Alice's account
bankAlice.deposit(5000)
# Show the balance of both accounts
bankAlice.show_balance()
bankBob.show_balance()

# Have Alice transfer $500 to the Bob
is_tranfer_successful = bankAlice.transfer_money(500, bankBob)
# Show the balance of both accounts after the transfer
bankAlice.show_balance()  
bankBob.show_balance()

# if the transfer was successful, have Alice request $250 from Bob
if is_tranfer_successful:
    is_request_successful = bankAlice.request_money(250, bankBob)
    # Show the balance of both accounts after the request
    bankAlice.show_balance()  
    bankBob.show_balance()
