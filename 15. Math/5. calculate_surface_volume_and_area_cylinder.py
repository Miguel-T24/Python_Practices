# 5. Wrote a python program to calculate the surface volume and area of a cylinder

import math

height = float(input("Height of Cylinder: "))
radian = float(input("radian of Cylinder: "))
volume = math.pi * radian * radian * height
sur_area = ((2*math.pi*radian) * height) + ((math.pi*radian**2)*2)

print("Volume is: {}".format(volume))
print("Surface Area is : {}".format(sur_area))
