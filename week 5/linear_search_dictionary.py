"""
# Linear Search in a Dictionary
# by Mathias Adikpon
# last updated: 07/13/2025
"""

def linear_search_dictionary(dictionary, target):
    """
    Perform a linear search in a dictionary to find the target value.
    """
    for key in dictionary:
        if dictionary[key] == target:
            print(f"Found at key {key}")
            return key
    print("Target is not in the dictionary")
    return None


""" driver code """

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)