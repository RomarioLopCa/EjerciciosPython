__author__ = 'romarinpc'


# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(*numbers):
    n1 = numbers[0]
    n2 = numbers[1]
    n3 = numbers[2]

    if n1 > n2:
        return n1 if n1 > n3 else n3
    elif n2 > n1:
        return n2 if n2 > n3 else n3


print(max_of_three(3, 1, 2))
print(max_of_three(10, 8, 1034))
print(max_of_three(-3, 6, 5))
print(max_of_three(-1, 5, 0))
