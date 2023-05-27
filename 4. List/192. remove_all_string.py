# 192. Write a python program to remove all strings from a given lists of tuples

l = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
temp = []
result = []

for i in l:
    for v in i:
        if type(v) != str:
            temp.append(v)
    result.append(temp)
    temp = []

result = list(map(lambda x:tuple(x),result))

print(result)
