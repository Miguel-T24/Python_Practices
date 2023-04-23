# 22. Write a pyhton  program to remove an empty tuple from a list of tuples

lista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Original List: {}".format(lista))

lista = [t for t in lista if t]
print("New list: {}".format(lista))

