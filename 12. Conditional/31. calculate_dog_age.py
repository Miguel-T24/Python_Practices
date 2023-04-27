# 31. Write a python program to calculate a dog's age in a dog years

def dog_year(age):
    return ((age-2)*4 + 10.5*2,10.5*age)[age<2]

print(dog_year(15))