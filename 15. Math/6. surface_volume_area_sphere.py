# 6.  Write a python program to calculate the surface volume and area of a sphere

import math

radius = float(input("Enter the radius of the sphere: "))

a = 4 * math.pi * radius**2
v = (4/3)*math.pi *radius**3

print("The area : {}\nThe Volume is : {}".format(a,v))
