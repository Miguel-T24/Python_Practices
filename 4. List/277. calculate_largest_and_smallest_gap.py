# 27. Write a python program to claculate the largest and smallest gap between sorted elements of a lists of integers

l = [1, 2 ,9, 0, 4, 6]
l.sort()

r = []
for i in range(len(l)-1):
    r.append(l[i+1] - l[i])
print(l)
print(max(r))
