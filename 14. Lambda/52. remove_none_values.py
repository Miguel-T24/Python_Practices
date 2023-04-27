# 52. Write a python program to remove None values from a given list using lambda function

lista = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

print("Original:",lista)
print(list(filter(lambda x:x is not None, lista)))