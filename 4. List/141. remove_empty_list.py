# 141. Write a python program to remove empty lists from given list of lists

list1 = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
result = list(filter(lambda x:len(x)!=0,list1))
print(result)