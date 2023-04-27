# 35. Write a python program that checks whetehr a string represents an integer or not

def int_or_not(num):
    return ("Isn't Integer", "IS INTEGER!")[num.isnumeric()]

print(int_or_not("50")) 
print(int_or_not("Python")) 