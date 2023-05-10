# 30. Write a python program to abbreviate 'Road' as 'Rd'. in a given string

from re import sub

text = '21 Ramkrishna Road'

# way 1
result = sub("Road","Rd",text)
print(result)

text = '21 Ramkrishna Road'

# way 2
result = text.replace("Road","Rd")
print(result)
