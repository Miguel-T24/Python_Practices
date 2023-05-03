# 61. Write a python programt o count the frecuency of a dictionary

from collections import Counter

dic = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

print("Original: {}".format(dic))
print("Counter: {}".format(Counter(dic.values())))

