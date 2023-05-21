# 86. Write a python program to create a 3x3 grid with numbers

import random as r

result = [[r.randint(0,9),r.randint(0,9),r.randint(0,9)] for i in range(3)]

print(result)