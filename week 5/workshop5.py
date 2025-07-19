import random

def guess_random_number(tries, start, stop):
    """Guess a random number between start and stop."""
    # Generate a random number between start and stop
    target = random.randint(start, stop)

    while tries != 0:
        # Print the number of tries left
        print(f"Number of tries left: {tries}")
        # Ask the user to guess the number
        guess = int(input(f"Guess a number between {start} and {stop}: "))

        # Check if the guess is correct
        if guess == target:
            print("You guessed the correct number!")
            return
        elif guess > target:
            print("Guess higher!")
        else:
            print("Guess lower!")

        # Decrease the number of tries left
        tries -= 1
    
    if tries == 0:
        print(f"You have failed to guess the number: {target}")


""" driver code """
guess_random_number(3,0,10)