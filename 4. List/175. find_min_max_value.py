# 175. Write a python program to find the minimum and maximum valu for each tuple position in a given lists of tuples

l = [(2, 3), (2, 4), (0, 6), (7, 1)]

print([max(dict(l).keys()),max(dict(l).values())])