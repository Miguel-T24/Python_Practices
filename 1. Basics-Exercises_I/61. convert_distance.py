# 61. write a python program to convert the distance (in feet) to inches, yards, and miles


feet = 100

inches = feet * 12
yards = feet / 3.0
miles = feet/ 5280

print("Inches: {:.2f} \nYards: {:.2f}\nMiles: {:.2f}".format(inches, yards, miles))
