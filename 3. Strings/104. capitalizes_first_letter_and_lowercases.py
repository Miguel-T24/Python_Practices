# 104. Write a python program that capitalizes the first letter and lowercases the remaining letters in a given string

def capitalize_first_letter(string):
    return " ".join(map(lambda x:x[0].upper() + x[1:].lower(),string.split(" ")))

print(capitalize_first_letter("Red Green WHITE"))
print(capitalize_first_letter("w3resource"))
print(capitalize_first_letter("dow jones industrial average"))