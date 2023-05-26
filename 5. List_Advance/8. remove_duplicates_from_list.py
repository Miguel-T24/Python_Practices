# 8. Write a python function to remove duplicates form a list while presserveing the order

list1 = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

print("Original\n{}".format(list1))
print("Duplicates Removed:\n{}".format(list(sorted(set(list1),key=list1.index))))
