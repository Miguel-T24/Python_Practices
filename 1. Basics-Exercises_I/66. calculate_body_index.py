# 66. Write a python program to calculate the body mass index

kilogram = float(input("Enter your kilogram: "))
feet = float(input("Enter your feet : "))

bmi = kilogram / feet**2

print("Your Mass Index is {:.2f}".format(bmi))
