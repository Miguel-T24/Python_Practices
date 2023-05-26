# 177. Write a python program t find common elements in a given lists of lists

l = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]

result = []
for i in range(len(l[0])):
    if(l[0][i] in l[1] and l[0][i] in l[2]):
        result.append(l[0][i])

print(result)