"""
# workshop3.app
# Mathias Adikpon
Juily, 5 2025
"""

from donations_pkg.homepage import show_homepage

# Declare variables
database = {"admin": "", "password": "password123"}  
donations = []
authorized_user = ""

# Call the homepage function
show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")
