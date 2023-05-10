# 22. Write a python program to find the occurrence and position of substrings within a string

from re import finditer

string = "hello world, how are you, hello, hello hello"
sub = "hello"

result = finditer(sub,string)

print("Ocurrence of {}: is: {}".format(sub,result))
print("Positions: ")

for i in result:
    print(i.group(),":",i.span())
