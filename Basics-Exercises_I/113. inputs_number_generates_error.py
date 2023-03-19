# 113. Write a python program that inputs a number and generates an error message if it is not a number

while True:
    try:
        a = int(input("Input a number: "))
        print(a)
        break
    except ValueError:
        print("This is not a number. Try again")