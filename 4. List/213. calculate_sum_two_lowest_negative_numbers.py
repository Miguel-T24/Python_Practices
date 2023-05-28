# 213. Write a python program to caluclate the sum of two lowest negative numbers ina given array of integers

l = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
print(l)
result = list(filter(lambda x:x<0, sorted(l)))
result = result[0] + result[1]

print(result)