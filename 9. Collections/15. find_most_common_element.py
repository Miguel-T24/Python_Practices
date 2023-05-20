# 15. Write a python program to find the most common element in a given list

import collections

lista = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']

print(collections.Counter(lista).most_common(1)[0][0])