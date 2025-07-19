import random
# Task 1
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

# Task 2: Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    """Guess a random number between start and stop."""
    # Generate a random number between start and stop
    target = random.randint(start, stop) 
    print(f"The number for the program to guess is : {target}")

    # Linear search of target
    for guess in range(start, stop + 1, 1):
        



# """ driver code """
# guess_random_number(5,0,10)