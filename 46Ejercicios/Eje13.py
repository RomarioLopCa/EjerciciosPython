__author__ = 'romarin'


# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
# numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance
# how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max


print(max_in_list([0, 6, 3, -1, 9, 12, 4, 123, 123, 432, 234, 345345]))
