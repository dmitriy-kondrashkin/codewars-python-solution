from math import sqrt

def is_square(n):
    return sqrt(n).is_integer() if n >= 0 else False

print(is_square(2))