# 29. Write a python program to find the maximum value in a ggiven heterogeneous list using lambda

list1 = ['Python', 3, 2, 4, 5, 'version']

result = max(list(filter(lambda x:str(x).isnumeric(),list1)))
print(result)