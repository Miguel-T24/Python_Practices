# 3. Write a python program to calculate the area of a trapezoid

height = float(input("Hieght of trapezoid: "))
base_1 = float(input("Base one values: "))
base_2 = float(input("base two values: "))

area = ((base_1 + base_2) / 2 ) * height

print("Area is : {}".format(area))
