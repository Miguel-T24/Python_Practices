# 98. Write a python program to decapitalize first letter of a given string.

def decapitalize(string):
    return string[:1].lower() + string[1:]

print(decapitalize("Java Script"))
print(decapitalize("Python"))