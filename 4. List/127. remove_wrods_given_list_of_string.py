# 127. Write a python program to remove words from a given list of stirngs containing a character or string

from re import sub

list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
list2 = ['#', 'color', '@']

rex = "("+"|".join(list2)+")"
print(rex)
result = list(map(lambda x:sub(rex,"",x).strip(),list1))
print(result)