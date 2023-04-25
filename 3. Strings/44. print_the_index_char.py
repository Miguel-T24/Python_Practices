# 44. Write a python program to print the index of a characater in a string

string = "hola mundo"

print(string.index("o"))

for index, char in enumerate(string):
    print(index , char)