# 3. Write a python program to get a string made of the firts 1 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead

def return_string(string):
    if(len(string)<2):
        return "Empty String"
    else:
        return string[0:2] + string[-2:]
    
print(return_string("w3resource"))
print(return_string("w3"))
print(return_string("w"))