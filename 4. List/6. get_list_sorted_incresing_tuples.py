# 6. Write a python program to get a list, sorted in incresing order by the last element in each tuple from given list of non-empty tuples

lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


for i in range(len(lista) - 1):
    for j in range(i+1,len(lista)):
        if (lista[j][1]<lista[i][1]):
            lista[i] , lista[j] = lista[j] , lista[i]

print(lista)