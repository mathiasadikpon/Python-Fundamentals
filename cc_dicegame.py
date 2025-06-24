'''Dice Game
This is a simple dice game where the user can roll two dice and keep track of the highest score achieved.'''
import random

# global variable to keep track of the high score
high_score = 0


def dice_game():
    try:
        # Display the current high score and options
        global high_score
        print(f"Current High Score: {high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        user_choice = int(input("Enter your choice: "))

        # Check if the user wants to leave the game
        if user_choice == 1:
            # Roll the two dice
            roll1 = random.randint(1, 6)
            print(f"\nYou roll a... {roll1}")
            roll2 = random.randint(1, 6)
            print(f"You roll a... {roll2}\n")

            #total score calculation
            total = roll1 + roll2
            print(f"You have rolled a total of: {total}\n")

            # Check if the total is greater than the high score
            if total > high_score:
                high_score = total
                print("New High Score!\n")
            
            dice_game()  # Call the function again to continue the game
        elif user_choice == 2:
            print("Goodbye!")
            return
        else:
            print("\nInvalid choice. Please try again.\n")
            dice_game() # Call the function again for a valid choice
    except ValueError:
        # Handle the case where input is not a number
        print("\nInvalid input. Please enter a number.\n")
        dice_game()  # Call the function again for valid input
    

# Start the game
dice_game()
