__author__ = 'romarinpc'


# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
# construct available in Python. (It is true that Python has the max() function built in, but writing it yourself
# is nevertheless a good exercise.)

def max(n1, n2):
    return n1 if n1 > n2 else n2


print(max(3, 5))
print(max(3, 1))
print(max(-1, -3))
print(max(0, 123))
print(max(0, 0))
