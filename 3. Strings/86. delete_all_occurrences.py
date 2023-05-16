# 86. Write a python program to delete all occurrence of specific character in given string

string = "Delete all occurrences of a specified character in a given string"
char = "a"
result = "".join(filter(lambda x:x!=char,string))

print(result)

# Second way
result = string.replace(char,"")
print(result)