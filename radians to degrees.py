# Byron Garcia
# 2/25/24
# will convert radians to degrees
import math

radians = float(input('What is your radians? '))
degree_calc = radians * (180 / math.pi)
degree = math.degrees(radians)
print('radians', radians)
print('radians to degrees with formula', degree_calc)
print('radians to degrees with module', degree)