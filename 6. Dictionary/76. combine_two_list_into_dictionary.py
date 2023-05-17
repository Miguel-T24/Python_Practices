# 76. Write a python program to combine two lists into a dictionary. The elemetns of the first one sereve as keys and the elements pf second one serve as value. Each item in the first list must be unique and hashable

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5]

result = dict(map(lambda x,y: (x,y), list1,list2))

print(result)