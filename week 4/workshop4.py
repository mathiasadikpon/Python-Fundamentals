
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
        print(f"{self.name.capitalize()} has an account balance of: {private_formatter(self.balance)}")

    def withdraw(self, amount: 'float'):
        """Withdraws the specified amount from the BankUser's balance"""
        if amount < 0:
            print(f"{self.name.capitalize()} cannot withdraw a negative amount: {private_formatter(amount)}")
        elif amount > self.balance:
            print(f"{self.name.capitalize()} cannot withdraw {private_formatter(amount)}. Insufficient funds.")
        else:
            self.balance -= amount
            # print(f"{self.name.capitalize()} withdrew {amount:.1f}. New balance: {self.balance:.1f}")

    def deposit(self, amount: 'float'):
        """Deposits the specified amount to the BankUser's balance"""
        if amount < 0:
            print(f"{self.name.capitalize()} cannot deposit a negative amount: {private_formatter(amount)}")
        else:
            self.balance += amount
            # print(f"{self.name.capitalize()} deposited {amount:.1f}. New balance: {self.balance:.1f}")

    def transfer_money(self, amount:'float', receiver: 'BankUser'):
        """Transfers the specified amount to another BankUser's balance"""
        print()
        print(f"You are transferring ${private_formatter(amount)} to {receiver.name.capitalize()}")
        # Authenticate the pin of the sender: sender is "self"
        print("Authentication required")
        pin = input("Enter your PIN: ").strip()
        if pin.isdigit() and int(pin) == self.pin:
            print("Transfer authorized")
            print(f"Transferring ${private_formatter(amount)} to {receiver.name.capitalize()}")
            self.withdraw(amount)
            receiver.deposit(amount)
            return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False        
          
    def request_money(self, amount: 'float', sender: 'BankUser'):
        """Requests the specified amount from another BankUser's balance bse on User receiving's pin and vlalide password of user requesting the money"""
        print()
        print(f"You are requesting ${private_formatter(amount)} from {sender.name.capitalize()}")
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
                print(f"{sender.name.capitalize()} sent ${private_formatter(amount)}")
                return True
            else:
                print("Invalid password. Transaction canceled.")
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            return False
        
def private_formatter(value: float | int):
    """Formats the value to 1 decimal place if it is a float, otherwise returns the whole number if it is an integer. all returns value as a string."""
    if value % 1 == 0:
        return f"{value:.0f}"
    else:
        return f"{value:.1f}"
    

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
