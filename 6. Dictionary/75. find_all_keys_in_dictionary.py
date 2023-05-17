# 75. Write a python program to find all keys in a dictionary that have the given value

dict1 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

result = list(filter(lambda x:dict1[x] == 20,dict1.keys()))
print(result)