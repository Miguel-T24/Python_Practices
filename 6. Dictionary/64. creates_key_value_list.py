# 664. Write a python program that reates key-value list pairing within a dictionary

dictionary = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

result = [dict(map(lambda x:(x,dictionary[x][0]),dictionary.keys()))]

print(result)