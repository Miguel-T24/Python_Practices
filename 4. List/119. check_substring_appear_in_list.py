# 119. Write a python program to checj if substring appears in a given list of string values

list_string = ['red', 'black', 'white', 'green', 'orange']

result = any(list(map(lambda x:'ack' in x,list_string)))
print(result)
result = any(list(map(lambda x:'abc' in x,list_string)))
print(result)