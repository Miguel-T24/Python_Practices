# 24. write a python program to check whether a string starts with a specified charcaters

def check_string_start(string, start):
    return string[0:len(start)] == start

print(check_string_start("w3cresource","w3c"))
print(check_string_start("w3cresource","w3a"))