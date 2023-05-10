# 18. Write a python program to search for numbers (0-9) of length between 1 and 3 in a given string

from re import finditer, findall

# Way 1l
def test(string):
    return finditer("\d{1,3}", string)

iterator = test("Exercises number 1, 12, 13, and 345 are important")

for i in iterator:
    print(i.group())

# Way 2
def test2(string):
    return findall("\d{1,3}", string)

list1 = test2("Exercises number 1, 12, 13, and 345 are important") 
for i in list1:
    print(i)