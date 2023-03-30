# 9. Write a python program to calculate the discriminant value

a_value = float(input("Enter value a: "))
b_value = float(input("Enetr value b: "))
c_value = float(input("Enter value c: "))

discriminant = (b_value**2) - (4*a_value*c_value)

if discriminant > 0:    
    print("Two Solutions. Discriminant value is: {}".format(discriminant))
elif discriminant == 0:
    print("One Solution. Discriminant value is: {}".format())
else:
    print("No real Solutions. Discriminant value is : {}".format(discriminant))
    