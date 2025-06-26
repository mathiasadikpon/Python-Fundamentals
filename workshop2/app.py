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


print("    === Automated Teller Machine ===    ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")