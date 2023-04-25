# 47. Write a python program to lowercase the first n characters in a string

string = 'The QUICK BROWN fox jumps over the lazy dog'
n = 9

string = list(string)

for i in range(n):
    string[i] = string[i].lower()

string= "".join(string)
print(string)


# Second way, and more easy

string = 'The QUICK BROWN fox jumps over the lazy dog'
print(string[:n].lower() + string[n:])