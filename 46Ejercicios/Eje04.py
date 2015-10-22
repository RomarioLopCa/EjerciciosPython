__author__ = 'romarinpc'


# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

vowels = 'aeiou '


def vowel(char):
    return True if char in vowels else False


print(vowel('a'))
print(vowel('e'))
print(vowel('s'))
print(vowel(' '))