# 57. Write a python program to check if all items in a given list of string are equal to given string

numeros1 = [1,2,3,4,5]
numeros2 = [7,7,7,7,7,7]

print(all(list(map(lambda x : x == 1,numeros1)))) # False
print(all(list(map(lambda x : x == 7,numeros2)))) # True
