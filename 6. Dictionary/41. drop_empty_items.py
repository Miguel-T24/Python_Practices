# 41. Write a python program to drop empty items frorm a given dictionary

dic = {'c1': 'Red', 'c2': 'Green', 'c3': None}

result = dict(filter(lambda x:x[1]!=None, dic.items()))

print(result)