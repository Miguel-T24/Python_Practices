# 69. Write a python program to remove duplicates from a list of list

lista = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
empty = []

for i in lista:
    if(i not in empty):
        empty.append(i)

print(empty)
