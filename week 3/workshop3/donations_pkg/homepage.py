"""
# workshop3.homepage
# Mathias Adikpon
Juily, 5 2025
"""

def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")

    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register        |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations  |")
    print("------------------------------------------")
    print("|            5.    Exit                   |")
    print("------------------------------------------")


def donate(username):
    """Function to handle donations."""
    donation_amt = float(input("\nEnter amount to donate: "))
    donation_string = f"{username} donated ${donation_amt:.1f}"
    print(f"Thank you for your donation!")
    return donation_string