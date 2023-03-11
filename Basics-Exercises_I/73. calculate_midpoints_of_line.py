# 73. Write a python program to calculate the midpoints of line

# midpoint formula ( (x1 + x2) / 2  ) , ( (y1 + y2) / 2 )

x1 = float(input("Enter x1: "))
y2 = float(input("Enter y2: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))

result = "("+ str((x1 + x2) / 2) +") , ("+ str((y1+y2)/2) +")"

print("{}".format(str(result)))