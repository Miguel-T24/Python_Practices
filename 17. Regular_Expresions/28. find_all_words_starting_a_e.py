# 28. Write a python program to find all words starting with a or e in a given string

from re import findall

string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = findall("[ae]\w+", string)

print(result)
