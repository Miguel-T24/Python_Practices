# 174. Write a pythjon program to add numebr to each element in a given list of numebrs


lista = [3, 8, 9, 4, 5, 0, 5, 0, 3]

print("Original\n",lista)
result = list(map(lambda x:x+3,lista))
print(result)