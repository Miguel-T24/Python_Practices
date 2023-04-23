# 28. Write a python program to convert tuple of string values to tuple of integers values.

tupla = (('333', '33'), ('1416', '55'))
tupla = list(tupla)

for i in range(len(tupla)):
    tupla[i] = list(tupla[i])
    for j in range(len(tupla[i])):
        tupla[i][j] = int(tupla[i][j])
    tupla[i] = tuple(tupla[i])
tupla = tuple(tupla)
print("Tupla: {}".format(tupla))
