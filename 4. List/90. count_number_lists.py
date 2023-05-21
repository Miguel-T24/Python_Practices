# 90. Write a python program to count the number of list in given lists of lists

lista = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]

result = len(list(filter(list,lista)))
print(result)

lista  = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
result = len(list(filter(list,lista)))
print(result)