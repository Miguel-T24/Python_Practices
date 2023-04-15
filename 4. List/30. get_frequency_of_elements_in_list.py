# 30. Write a python program to get the frequency of element in a list

lista = [1,1,2,2,3,3]

lista1 = list(set(lista))

for i in lista1:
    print("frequence of {}: {}".format(i,lista.count(i)))