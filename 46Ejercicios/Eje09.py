__author__ = 'romarinpc'


# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns
# True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake
# of the exercise you should pretend Python did not have this operator.)

def is_member(number, list):
    for item in list:
        if number == item:
            return True
    return False


print(is_member('s', [5, 4, 3, 2, 's']))
