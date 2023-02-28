# 21. Write a python program that determinates whether a given number (accepted from the user) is even or odd, and prints an appropiate message to the user.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))