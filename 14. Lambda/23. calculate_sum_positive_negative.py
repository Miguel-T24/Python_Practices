# 23. Write a python program to calculate the sum of the positive and negative numebrs of a given list of numbers using the lambda function

lista = [2, 4, -6, -9, 11, -12, 14, -5, 17]

result = sum(list(filter(lambda x:x>=0,lista)))
print("Sum of positive numbers: {}".format(result))
result = sum(list(filter(lambda x:x<0,lista)))
print("Sum of negative numbers: {}".format(result))
