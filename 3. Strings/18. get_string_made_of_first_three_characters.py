# 18. Write a python function to get a string made of the first three chcracters of a specified string. if length of string is less than 3, return the original string.

def three_first_string(string):
    return (string,string[:3])[len(string) > 3]


print(three_first_string("ipy"))
print(three_first_string("Python"))

