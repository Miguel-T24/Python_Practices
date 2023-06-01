# 43. Write a pytohon program to find maximum fifference bwteen pairs in a given lists

from itertools import combinations

l = [32, 14, 90, 10, 22, 42, 31]

l = list(combinations(l,2))

max_dif = max(l, key=lambda x:abs(x[0]-x[1]))

print(max_dif)
