# 63. Write a python program to convert a given list of list to a dictionary.

list_list= [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

result = dict(map(lambda x:(x[0],[x[1],x[2]]), list_list))

print(result)