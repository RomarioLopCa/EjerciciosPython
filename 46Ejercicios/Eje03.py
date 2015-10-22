__author__ = 'romarinpc'


# Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)

def len_str(string):
    n = 0
    characters = list(string)
    for ch in characters:
        n += 1
    return n


print(len_str("Romario"))