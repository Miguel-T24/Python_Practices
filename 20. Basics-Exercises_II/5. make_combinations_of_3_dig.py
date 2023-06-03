# 5. Write a python program to make combinatios of 3 digits.

numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)
