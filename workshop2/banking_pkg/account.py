
def  show_balance(balance):
    """Display the current balance of the account."""
    print(f"Current balance: ${balance}")
    # print(f"Current balance: ${balance:.2f}") specific formatting with 2 decimal places


def deposit(balance):
    """Deposit money into the account."""
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        # print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Invalid deposit amount.")
    return balance


def withdraw(balance):
    """Withdraw money from the account."""
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        # print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance


def logout(name):
    """Logout the user."""
    print(f"Goodbye {name}!")
