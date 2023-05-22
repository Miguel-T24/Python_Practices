# 110. Write a python program to find the item with the most occurrence in a given list

from collections import Counter

lista = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

print(Counter(lista).most_common())
print(Counter(lista).most_common(1))