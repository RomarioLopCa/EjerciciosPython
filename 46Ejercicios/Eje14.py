__author__ = 'romarin'


# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

def map_list_with_ints(list):
    new_list = []
    for item in list:
        new_list.append((item, len(item)))
    return new_list


print(map_list_with_ints(['Romario', 'Edu']))
