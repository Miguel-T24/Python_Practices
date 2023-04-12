# 18. Write a python program to find palindromes in a given list of string using lambda

array = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindrom = list(filter(lambda x:x==x[-1::-1], array))

print(palindrom)