# 101. Wrte a python program to sort a goven matrxi in ascending order according to the sum of its rows

lista = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

result = sorted(lista, key=lambda x:sum(x))

print(result)