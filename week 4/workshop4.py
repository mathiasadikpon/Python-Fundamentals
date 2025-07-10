
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