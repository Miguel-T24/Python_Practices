# 94. Write a python program to count the number of unique sublist within a given lists

from collections import Counter

lista  = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
result = Counter(map(lambda x:tuple(x),lista))

print(result)