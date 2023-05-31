# 20. Write a python program to find the factorial of number using the itertools module
from itertools import accumulate
from operator import mul

fac = 4
result = list(accumulate(list(range(1,fac+1)), mul))

print(result[-1])
