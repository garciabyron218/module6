# Byron Garcia
# 2/25/24
# will show factorial from input value
import math


def factorial (x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

x = int(input('what is your value? '))

factorial_calc = math.factorial(x)

print('formula factorial answer', factorial(x))
print('module factorial answer', factorial_calc)
