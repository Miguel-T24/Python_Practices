# 46. Write a python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists

lista = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
keys = list(set(map(lambda x:x[0],lista)))
print("Original list:",lista)
print("the keys are:",keys) # ['red','yellow','blue']

result = {}
for i in range(len(keys)):
    for j in range(len(lista)):
        if keys[i] == lista[j][0]:
            temp = list(filter(lambda x:x[0]==keys[i],lista))
            result[keys[i]] = list(map(lambda x:x[1],temp))

print(result)