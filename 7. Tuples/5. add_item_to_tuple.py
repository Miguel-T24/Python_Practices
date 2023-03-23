# 5. Write a python program to add an item to a tuple

tup = (1,2,3,4)
print("Original:", tup)

tup = tup + (5,)
print("Add 5 :",tup)

print(tup[:3] + (5,) + tup[:3])

print("Converting tuple to list:",list(tup))

# We can convert tuple to list, use lst methods and convert list to tuple

lista_tupla = list(tup)
lista_tupla.append(6)
tup = tuple(lista_tupla)

print("Conversion de tupla a lista y lista a tupla:",tup)