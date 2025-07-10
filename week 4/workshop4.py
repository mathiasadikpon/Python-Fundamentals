
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password


""" Driver Code for Task 1 """
# user "Bob" as the name, 1234 as the pin, and "password" as the password
user = User("Bob", 1234, "password")
print(f"{user.name} {user.pin} {user.password}")