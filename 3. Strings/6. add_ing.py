# 6. Write a python program to add "ing" at the end of given string (length should be at least 3). if the given string already ends with 'ing', add 'ly instead. if the string length of the given string is lees than3, leave it unchanged


def add_string(stri):
    if(len(stri) < 3):
        return stri
    elif(stri[-3:] != 'ing'):
        return stri + 'ing'
    elif(stri[-3:] == "ing"):
        return stri+"ly"
    
print(add_string("abc"))
print(add_string("string"))

