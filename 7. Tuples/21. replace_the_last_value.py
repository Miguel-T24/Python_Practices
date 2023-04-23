# 21. Write a python program to replace the lasts of tuples in a list

tupla = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print("Original List: {}".format(tupla))

tupla[2] = list(tupla[2])
tupla[2][2] = 100
tupla[2] = tuple(tupla[2])

print("New List: {}".format(tupla))
