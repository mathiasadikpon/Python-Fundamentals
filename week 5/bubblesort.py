"""
# bubble sort algorithm
# by Mathias Adikpon
# last updated: 07/13/2025
"""

def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx - i):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
     
""" driver code """
unsorted_list = [49, 101, 3, 12, 56]
bubblesort(unsorted_list)