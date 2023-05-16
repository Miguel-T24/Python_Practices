# 84. Write a python program to swap cases in a given string

def lower_upper_vice(string):
    return "".join(map(lambda x:(x.lower(),x.upper())[x.islower()],string))

print(lower_upper_vice("Python Exercises"))
print(lower_upper_vice("Java"))
print(lower_upper_vice("NumPy"))