# 10. write a python program that accepts an interer (n) and computes the value of n+nn+nnn

n = int(input("Enter number: "))

print("Sample value of n is ", n)
print("Result: " , n + int(str(n)*2) + int(str(n)*3) )