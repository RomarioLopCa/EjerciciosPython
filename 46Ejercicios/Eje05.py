__author__ = 'romarinpc'

import Eje04


# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".

def translate(string):
    new_str = ''
    for ch in list(string):
        if not Eje04.vowel(ch):
            new_str += ch + 'o' + ch
        else:
            new_str += ch
    return new_str

print(translate("this is fun"))
