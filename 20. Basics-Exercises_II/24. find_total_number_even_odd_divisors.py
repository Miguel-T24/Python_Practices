# 24. Write a python program to find the total number of even or odd divisors of a given interger

def divisor(n):
  x = len([i for i in range(1,n+1) if not n % i])
  return x
print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))