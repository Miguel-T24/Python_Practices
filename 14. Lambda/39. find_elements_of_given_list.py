# 39. Write a python program to find the elements of a given list of string that contain a specific substring using lambda

lista = ['red', 'black', 'white', 'green', 'orange']
print(list(filter(lambda x: "ack" in x , lista)))
print(list(filter(lambda x: "abc" in x , lista)))

