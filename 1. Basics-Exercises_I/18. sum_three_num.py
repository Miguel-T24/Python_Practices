# 18. Write a python program to calculate the sum of three given numbers. if the values area equal, return three times their sum


num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

if num1 == num2 and num2 == num3:
    print((num1 + num2 + num3) * 3)
else:
    print((num1 + num2 + num3))