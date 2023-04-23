# 23. Write a python program to sort a tuple by its float element

lista = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
lista = sorted(lista, key = lambda x:x[1], reverse= True)
print("new list: {}".format(lista))
