# 21. Write a python function to convert given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


def upperC(string):
    count = 0;
    for i in range(0,4):
        if string[i].isupper():
            count+=1
        if count == 2:
            return string.upper()
    return string

print(upperC("HOla"))
print(upperC("hola"))