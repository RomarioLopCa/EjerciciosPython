__author__ = 'romarinpc'

import Eje09


# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

def overlapping(list1, list2):
    for item in list1:
        if Eje09.is_member(item, list2):
            return True
    return False


print(overlapping([1, 2, 3], [4, 5, 6]))
