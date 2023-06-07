# 34. Write a python program to check whether three given lengths (integers) of three sides form a right triangle. print 'yes' if the given sides form a right triangle otherwise print 'no'

def form_triangle(n1,n2,n3):
    return 'Yes' if (n1+n2+n3)==180 else "No"

print(form_triangle(45,75,60))
print(form_triangle(45,75,40))