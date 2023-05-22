# 103. Write a python program oto extract specified number of elements from a given list which follows each other continuosly

lista  = [1, 1, 3, 4, 4, 5, 6, 7]
result = []

for i in range(len(lista)):
    if(i!=0):
        if(lista[i] == lista[i-1]):
            result.append(lista[i])
result = sorted(set(result), key=result.index)
print(result)