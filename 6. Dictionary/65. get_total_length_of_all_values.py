# 65. Write a python programt o get the total length of all values in a given dictionary with string values

dic = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
result = sum(list(map(lambda x:len(x), dic.values())))
print(result)