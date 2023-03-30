# 7. Write a python program to calculate the arc length of an angle

import math

diameter = float(input("Diameter of Circle: "))
angle = float(input("Angle Measure: "))

if angle >= 360:
    print("Angle is not possible")
else:
    arc_length = (math.pi*diameter) * (angle / 360)
    print("Arch Length is :",arc_length)
    