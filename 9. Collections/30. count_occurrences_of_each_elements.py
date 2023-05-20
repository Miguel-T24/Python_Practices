# 30. Write a python proram to count the occurrences of each element in a given list

from collections import Counter


l = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
print(Counter(l))
l = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
print(Counter(l))
