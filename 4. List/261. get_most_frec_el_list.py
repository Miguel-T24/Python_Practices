# 261. Write a python program to get the most frequent element in a given lkist of numbers
from collections import Counter
l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]

print(Counter(l).most_common(1)[0][0])