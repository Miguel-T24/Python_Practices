# 158. Write a python program to find the maxmimunm and minimum values in a given lists of tuples

lista = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]

find = list(map(lambda x:x[1],lista))

print(find)

print("Max: {}".format(max(find)))
print("Min: {}".format(min(find)))
