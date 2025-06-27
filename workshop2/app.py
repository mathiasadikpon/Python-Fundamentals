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

# Task 2
print("    === Automated Teller Machine ===    ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")
# end task 2

# Task 3
# Request the user's name an Pin for login
while True:
    print("\n    === Automated Teller Machine ===    ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print( "Invalid credentials!") 
