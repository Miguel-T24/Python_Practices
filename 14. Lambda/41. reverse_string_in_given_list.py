# 41. Write a python program to revese strings in a given list of stirng values using lambda

lista = ['Red', 'Green', 'Blue', 'White', 'Black']
print(list(map(lambda x:x[::-1], lista)))