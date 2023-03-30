# 1. Write a python program to convert degrees to radianss

import math

degree = int(input("Enter Dregees: "))
radians = degree*(math.pi/180)

print("Degrees : {} in Radians : {:.2f}".format(degree,radians))
