# 9. Write a python program to iterate over dictionaries using for loops

dic = {1:"a" , 2:"b"}

for keys , values in dic.items():
    print("{} : {}".format(keys, values))

for i in dic:
    print("{} : {}".format(i,dic[i]))
    