# 190. Write a python program to find the specified number of a largest products from two given lists, multiplying an elenment from each list

l1 = [1, 2, 3, 4, 5, 6]
l2 = [3, 6, 8, 9, 10, 6]
r = []

for i in l1:
    for j in l2:
        r.append(i*j)

print(r)

r.sort(reverse=True)
print(r)

print("3 Number of largest products from the said two lists: {}".format(r[:3]))
print("4 Number of largest products from the said two lists: {}".format(r[:4]))
