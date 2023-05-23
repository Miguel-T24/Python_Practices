# 138. Write a python porgram to sort given mixed of integers an string

lista = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

result = sorted(list(filter(lambda x:isinstance(x,int),lista))) + sorted(list(filter(lambda x:isinstance(x,str),lista)), key=lambda x:x[0])

print(result)