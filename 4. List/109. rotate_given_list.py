# 109. Write a python program to rotate given list by specified number of items in the right or left direction

# way 1
from collections import deque
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original:\n{}".format(lista))
lista = deque(lista)

lista.rotate(-4)
print("Rotate by 4:\n{}".format(list(lista)))

# way 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original:\n{}".format(lista))
print("Roatte by 4:\n{}".format(lista[4:] + lista[:4]))
