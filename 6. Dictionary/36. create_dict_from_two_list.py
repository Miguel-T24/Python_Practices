# 36. Write a python program to create a dcitionary form twi lists without losing duplicate values

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]
dic = dict()

for l1,l2 in zip(list1,list2):
   dic.update({l1:l2}) 

print(dic)
