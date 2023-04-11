# 11. Write a python program to multiply all the items in a dictionary


dictionary = {"a":1, "b":2, "c" :3 }
result = 1

for x in list(dictionary.values()):
    result = result * x

print(result)