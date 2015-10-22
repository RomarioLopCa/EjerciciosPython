import string

__author__ = 'romarin'


# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a
# lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the
# exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

def palindrome_phrases(phrase=''):
    phrase = phrase.replace(' ', '')
    phrase = phrase.translate(string.maketrans("", ""), string.punctuation)
    phrase = phrase.lower()
    print(phrase)
    return phrase == phrase[::-1]


print(palindrome_phrases("I roamed under it as a tired nude Maori"))
print(palindrome_phrases("Dammit, I'm mad!"))
