__author__ = 'romarin'

import Eje11


# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******


def histogram(list):
    for item in list:
        print(Eje11.generate_n_chars(item, '*'))


histogram([4, 9, 7])
