# 14. Write a python program to filter a given list to determine if the values in the list have a length of 6 using lambda function.

array = ["Monday","Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]

six = list(filter(lambda x:len(x)==6,array))

print(six)