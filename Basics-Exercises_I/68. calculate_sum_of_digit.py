# 68. Write a python program to calculate sum of digit of a number

number = input("Enter a number: ")
number = list(number)
number = [int(x) for x in number]

print("The sum is {}".format(sum(number)))
