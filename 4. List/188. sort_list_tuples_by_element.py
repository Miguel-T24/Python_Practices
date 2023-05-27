# 188. Write a python porgram to sort a given of tuples by a specified element

l = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
result = sorted(l,key=lambda x:x[0])
print(result)
result = sorted(l,key=lambda x:x[1])
print(result)