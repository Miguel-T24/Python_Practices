# 257. Wriet a python program to check if two given lists contain the same elements regardess of order

l1 = [1, 2, 4]
l2 = [2, 4, 1]

result = list(map(lambda x:x in l2,l1))
print(all(result))

l1 = [1, 2, 3]
l2 = [1, 2, 4]
result = list(map(lambda x:x in l2,l1))
print(all(result))
