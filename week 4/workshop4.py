
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
    
    def change_pin(self, new_pin):
        self.pin = new_pin
    
    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    """ BankUser class inherits from User class """
    
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        """Prints the BankUser object's balance"""
        print(f"{self.name.capitalize()} has an account balance of: {self.balance:.1f}")

    def withdraw(self, amount):
        """Withdraws the specified amount from the BankUser's balance"""
        if amount < 0:
            print(f"{self.name.capitalize()} cannot withdraw a negative amount: {amount:.1f}")
        elif amount > self.balance:
            print(f"{self.name.capitalize()} cannot withdraw {amount:.1f}. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.name.capitalize()} withdrew {amount:.1f}. New balance: {self.balance:.1f}")

    def deposit(self, amount):
        """Deposits the specified amount to the BankUser's balance"""
        if amount < 0:
            print(f"{self.name.capitalize()} cannot deposit a negative amount: {amount:.1f}")
        else:
            self.balance += amount
            print(f"{self.name.capitalize()} deposited {amount:.1f}. New balance: {self.balance:.1f}")


""" all driver code"""
   
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

""" Driver Code for Task 3"""
# bankBob = BankUser("Bob", 1234, "password")
# print(f"{bankBob.name} {bankBob.pin} {bankBob.password} {bankBob.balance}")

""" Driver Code for Task 4"""
