# 6. Write a python function to check whteher a number falls within a given range

def numbers_falls(num):
    if num in range(10,21):
        print("The number is in range of 10 and 20")
    else:
        print("The number isn't in range of 10 and 20")

numbers_falls(15)
numbers_falls(20)
numbers_falls(9)
