# 1212. Wrte a python program to remove all values except integer values fom a given array of mixed values

l =  [34.67, 12, -94.89, 'Python', 0, 'C#']
result = list(filter(lambda x:isinstance(x,int), l))
print(result)