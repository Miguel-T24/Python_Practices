# 56. Write a python program to convert a dictionary into a list of lists

dic = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

print(list(map(list,dic.items())))