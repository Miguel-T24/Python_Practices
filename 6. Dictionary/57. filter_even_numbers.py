# 57. Write a python program to filter even numbers form a dictionary of values

dic = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

result = dict(map(lambda x: (x[0], list(filter(lambda y:y%2==0,x[1]))) , dic.items()))

print("Original: {}".format(dic))
print("Filter: {}".format(result))
