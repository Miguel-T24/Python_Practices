# 44. Write a python program to do case-insensitive string replacement

# from re import sub

# string = "PHP Exercises"
# result = sub("PHP", "php", string)

# print(result)


import re
text = "PHP Exercises"
print("Original Text: ",text)
redata = re.compile(re.escape('php'), re.IGNORECASE)
new_text = redata.sub('php', 'PHP Exercises')
print("Using 'php' replace PHP") 
print("New Text: ",new_text)