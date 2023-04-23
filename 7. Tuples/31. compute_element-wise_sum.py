# 31 .Write a python program to compute the elemnt-wise sum of given tuples

tupla1, tupla2, tupla3 = (1, 2, 3, 4) , (3, 5, 2, 1) , (2, 2, 3, 1)

print("Tuples: \n{}\n{}\n{}".format(tupla1,tupla2,tupla3))
result = tuple(map(lambda x, y ,z : x + y + z, tupla1,tupla2,tupla3))
print("\nResult {} ".format(result))