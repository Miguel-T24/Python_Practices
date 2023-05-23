# 114. Write a ptyhon program to extract the nth element from a given list of tuple

list_tuple = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

result = list(map(lambda x:x[2], list_tuple))

print(result)