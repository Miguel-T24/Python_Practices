# 2. Wrte a python program to convert radians to degrees

import math

radians = float(input("Enter Radians: "))
degree = radians*(180/math.pi)

print("Raidnas : {} Degrees {:.3f}".format(radians,degree))


# Other Way
print("Raidnas: {} in degrees: {}".format(radians, math.degrees(radians)))
