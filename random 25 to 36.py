# Byron Garcia
# 2/25/24
# program will randomly give you a number between 25 and 36, 10 times


import random

for _ in range(10):
    random_integer = random.randrange(25, 36)
    print(random_integer)