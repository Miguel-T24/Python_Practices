# 154. Wriyte a python program to join two given lists of lists of the same length, element wise

list1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]

result = list(map(lambda x,y:x+y,list1,list2))

print(result)