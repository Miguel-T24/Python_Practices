# 163. Write a python program to get the index of the firts element that is greater than specified element

lista = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

result = lista.index(next(filter(lambda x:x>73,lista)))
print(result)
result = lista.index(next(filter(lambda x:x>21,lista)))
print(result)
result = lista.index(next(filter(lambda x:x>80,lista)))
print(result)
result = lista.index(next(filter(lambda x:x>50,lista)))
print(result)