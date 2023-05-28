# 220. Write a python program to map the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key  and the result of the function as the value

l = [1,2,3]

result = dict(map(lambda x:(x,x*x), l))
print(result)