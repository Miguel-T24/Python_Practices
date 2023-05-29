# 244. Write a Python program to initialize a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step. Return an error if step equals 1.

from math import floor, log
def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)] 
print(geometric_progression(256))
print(geometric_progression(256, 3))
print(geometric_progression(256, 1, 4))