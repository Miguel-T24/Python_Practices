# 1p4. Wroite a puython program to find the differencd between consecutive nubers in a given list

lista = [1, 1, 3, 4, 4, 5, 6, 7]

diff = []

for i in range(len(lista)):
    if(i!=0):
        diff.append(lista[i] - lista[i-1])

print(diff)