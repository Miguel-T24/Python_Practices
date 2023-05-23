# 116. Write a python porgram to sort a list of lists by given index of the inner list

lista =[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

print(sorted(lista, key=lambda x:x[0]))
print(sorted(lista, key=lambda x:x[2]))