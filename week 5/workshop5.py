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
    t = tries
    for guess in range(start, stop + 1, 1):
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {guess}")
        if guess == target:
            print("The program has guessed the correct number!")
            return
        tries -= 1

#Task 3: Guess the number programmatically using binary search
def guess_random_num_binary(tries, start, stop):
    """Guess a random number between start and stop."""
    # Generate a random number between start and stop
    target = random.randint(start, stop) 
    print(f"Random number to find: {target}")

    # Call Binary search of target
    the_list = list(range(start, stop + 1, 1))
    binary_search(tries, the_list, target)   

# binary search
def binary_search(tries, the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1
    while lower_bound <= upper_bound:
        if tries == 0:
            break
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        print(f"pivot_value: {pivot_value}")#see  pivo
        if pivot_value == target:
            print(f"Found it! {pivot_value}")
            return pivot
        if pivot_value > target:
            print("Guessing higher!")
            upper_bound = pivot - 1
        else:
            print("Guessing lower!")
            lower_bound = pivot + 1
        tries -= 1

    print("Your program has failed to find number.")
    return -1

# """ driver code """
# guess_random_number(5,0,10)
# guess_random_num_linear(5,0,10)
guess_random_num_binary(5,0,100)