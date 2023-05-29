# 224. Write a python program to crate a lists with unique values filytered out

l = [1, 2, 2, 3, 4, 4, 5]

result = list(set(list(filter(lambda x : l.count(x)>1,l))))

print(result)