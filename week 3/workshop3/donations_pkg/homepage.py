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
    try:
        donation_amt = float(input("\nEnter amount to donate: "))
        if donation_amt == 0:
            print("Donation amount cannot be zero. Please enter a valid amount.")
            return ""
        elif donation_amt < 0:
            print("Donation amount cannot be negative. Please enter a valid amount.")
            return ""
        else:
            donation_string = f"{username.capitalize()} donated ${donation_amt:.1f}"
            print(f"Thank you for your donation!")
            return donation_string
    except:
        print("Donation amount cannot be non-numeric. Please enter a valid amount.")
        return ""




def show_donations(donations):
    """Function to display all donations."""
    print( "\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        # Display all donations
        total_donations = 0
        for donation in donations:
            total_donations += float(donation.split('$')[1])
            print(donation)
        print(f"Total = ${total_donations:.1f}")