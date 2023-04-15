# 25. Write a python program to create caesar encryption

def caesar(string):
    new_string = ""

    for i in string:
        new_string += chr(ord(i) + 2) 

    return new_string


print(caesar("abc"))