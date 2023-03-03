# 26. Write a python program to add objects if both are integers

def add(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        return "Inputs must be integers!"
    return a + b

print(add(10,20))
print(add(10,20.23))
print(add('5',6))
print(add('5','6'))