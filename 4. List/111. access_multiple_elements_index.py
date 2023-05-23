# 111. Write a python program to access multiple elements at a specified index from a given list

lista = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
l_index = [0,3,5,7,10]


result = list(map(lambda x:lista[x],l_index))

print(result)