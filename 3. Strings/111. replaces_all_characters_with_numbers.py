# 111. Write a python program that takes a string and replaces all the characters with their respctive numbers.

def replace_char_number(string):
    string = string.replace(" ","")
    return " ".join(map(lambda x:str(ord(x.lower())-96), string))

print(replace_char_number("Python"))
print(replace_char_number("Java"))
print(replace_char_number("Python Tutorial"))