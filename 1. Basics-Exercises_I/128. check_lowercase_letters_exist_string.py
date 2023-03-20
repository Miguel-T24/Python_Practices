# 128. Write a python program to check whther lowercase letters exist in a string

string1 = "Hola Mundo"
string2 = "HOLAMUNDO"

def check_lower(string):
    for x in string:
        if(x == x.lower()):
            return True
    return False

print(check_lower(string1))
print(check_lower(string2))


print(any(x.islower() for x in string1))
print(any(x.islower() for x in string2))