# 23. Write a python program to get n copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

string = input("Enter string: ") 
n = int(input("Enter n: "))

if len(string) < 2:
    print(string * n)
else:
    for i in range(n):
        print(string[0:2], end = "")
    print()