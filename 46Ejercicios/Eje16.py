__author__ = 'romarin'


# Write a function filter_long_words() that takes a list of words and an integer n and returns the
# list of words that are longer than n.

def filter_long_words(limit, list=[]):
    for item in list:
        if len(item) < limit:
            list.remove(item)

    return list


print(filter_long_words(15, ['romario', 'asdasdasdsda']))
