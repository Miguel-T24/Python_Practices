# 59. Write a python program to convert heigth (in feet and inches) to centimeters


ft = int(input("Enter feet: "))
inch = int(input("Enter Inches: "))

inch += ft * 12
h_cm = round(inch * 2.54,1)

print("your height is : {} cm".format(h_cm))