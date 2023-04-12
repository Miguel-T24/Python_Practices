# 17. Write a python program to find numbers divisible by nineteen or thriteen from a list of numbers using lambda

array = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = list(filter(lambda x:(x%13==0 or x%19==0),array))

print(result)