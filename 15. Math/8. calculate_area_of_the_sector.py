# 8. Write a python program to calculate the area of the sector

import math

radius = float(input("Raiuds of circle: "))
angle = float(input("Angle Measure: "))
if angle >= 360:
    print("Angle is not posible")
else:
    sur_area = (math.pi*radius**2) * (angle / 360)
    print("Sector Area: ", sur_area)