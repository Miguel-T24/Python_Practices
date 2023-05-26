# 171. Write a python program to concatenate elemen-wise three goven lists

list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']

result = list(map(lambda x,y,z:x+y+z,list1,list2,list3))

print(result)