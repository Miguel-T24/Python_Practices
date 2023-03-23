# 5 Write a python program to iterate over dictionaries using for loops

dic = {1:"a" , 2 : "b"}

# way 1
for i in dic:
    print(i,":", dic[i])

# way 2

for key, value in dic.items():
    print(key, ":" , value)
    