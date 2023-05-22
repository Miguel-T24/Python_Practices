# 99. Write a python program to find the maximum and minimum values in a given heterogeneous list.

lista = ['Python', 3, 2, 4, 5, 'version']
lista = list(filter(lambda x: isinstance(x,int),lista))
maxv, minv = max(lista), min(lista)

print("Max: {}".format(maxv))
print("Min: {}".format(minv))