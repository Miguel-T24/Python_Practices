# 17. Write a python function to get a string made of 4 copies of the last twi charcaters of a specified string (length must be 2).

def copies(string):
    return (string, string[-2:] * 4 )[len(string) > 2]

print(copies('Python'))
print(copies('exercises'))
