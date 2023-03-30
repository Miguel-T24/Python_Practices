# 1. Write a python program to convert degrees to radianss

import math

degree = int(input("Enter Degrees: "))
radians = degree*(math.pi/180)

print("Degrees : {} in Radians : {:.2f}".format(degree,radians))

# Other Way
print("Degrees: {} in radians: {}".format(degree,math.radians(degree)))

