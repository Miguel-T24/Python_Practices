# 60 Write a python program to calculate the hypotenuse of a right angled triangle

import math

cat1 = int(input("Enter cat 1: "))
cat2 = int(input("Enter cat 2: "))

hypo = math.sqrt(cat1**2 + cat2 **2)

print("the hypotenuse is {}".format(int(hypo)))
