# 105. Write a python program to extract and display the name form a given email address

from re import match, sub

def extract_name(email):
    result = match(".+@",email).group()[:-1] 
    result = sub("[^A-Za-z]","",result)
    return result

print(extract_name("john@example.com"))
print(extract_name("john.smith@example.com"))
print(extract_name("fully-qualified-domain@example.com"))