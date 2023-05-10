# 29. Write a python program to separate and print the numbers and their position in a given string

from re import finditer

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = finditer("\d+",text)

for i in result:
    print(i.group(),":",i.span())