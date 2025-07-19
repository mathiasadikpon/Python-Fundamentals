import random

def guess_random_number(tries, start, stop):
    """Guess a random number between start and stop."""
    # Generate a random number between start and stop
    random_number = random.randint(start, stop)