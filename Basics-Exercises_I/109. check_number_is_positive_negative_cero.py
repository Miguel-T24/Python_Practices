# 109. Write a python program to check if a number is positive, negative or zero

number = int(input("Number: "))

result = (("Negative",
            "Positive")[number > 0],
            "Equal 0")[number==0]

print(result)