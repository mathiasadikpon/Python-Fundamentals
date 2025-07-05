#
from my_donations_pkg.user import User

class Donations:

    def __init__(self, database={User("admin","password123")}, donations=[], authorized_user=""):
        if database is not None:
            self.database = database
        if donations is not None:
            self.donations = donations
        self.authorized_user = authorized_user

    def show_homepage(self):
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
    
    def authorized_user(self):
        """Check if the user is authorized."""
        if self.authorized_user == "":
            print("You must be logged in to donate.")
        else:
            print(f"Logged in as: {self.authorized_user}")