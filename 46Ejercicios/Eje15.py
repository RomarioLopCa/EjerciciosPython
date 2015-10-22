__author__ = 'romarin'


# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def longest_word(list):
    long = 0
    for item in list:
        if len(item) > long:
            long = len(item)
    return long


print(longest_word(['Romario', 'Edu', 'Sumamamamammama']))
