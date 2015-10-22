__author__ = 'romarin'


# Represent a small bilingual lexicon as a Python dictionary in the following
# fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
# "new":"nytt", "year":"år"} and use it to translate your Christmas cards f
# rom English into Swedish. That is, write a function translate() that takes
# a list of English words and returns a list of Swedish words.

dictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",
              "new": "nytt", "year": "år"}


def translate(list=[]):
    new_list = []
    for item in list:
        if item in dictionary.keys():
            new_list.append(dictionary.get(item))
    return new_list


print(translate(['merry', 'year', 'asd']))
