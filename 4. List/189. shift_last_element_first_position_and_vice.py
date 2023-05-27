# 189. Write a pythonn program to shift last element to first position and first element to last position in a given list

l = [1, 2, 3, 4, 5, 6, 7]
print(l)
l = [l[-1]] + l[1:-1] + [l[0]]
print(l)