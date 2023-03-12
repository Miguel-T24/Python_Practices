# 82. Write a python program to calculate the sum of all items of a container (tuple, list set, dictionary)

lista = [1,2,3]
tupla = (1,2,3)
diccionario = {"a" : 1 , "b" : 2, "c" : 3}
conjunto = {1,2,3}

print("Lista: {}".format(sum(lista)))
print("Tupla: {}".format(sum(tupla)))
print("diccionario: {}".format(sum(diccionario.values())))
print("conjunto: {}".format(sum(conjunto)))

