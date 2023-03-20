# 16. write a program to calculate the diffrenec ebetween a given number and 17. if the number is greater than 17, return twice the absolute difference

num = int(input("Enter a number: "))

if num == 17:
    print("The number is 17")
elif num > 17:
    print("{}".format((num - 17) * 2))
else:
    print("{}".format(17-num))