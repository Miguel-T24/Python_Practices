# 34. Write a python program to compute the sum of digits of each number in a igven list of positive integers

from itertools import chain

# way 1
l = [10, 2, 56]
l = [str(x) for x in l]
l = "".join(l)
r = sum([int(x) for x in l])
print(r)

# way 2 with itertools

l = [10, 2, 56]
r = sum([int(y) for y in list(chain(*[str(x) for x in l]))])
print(r)