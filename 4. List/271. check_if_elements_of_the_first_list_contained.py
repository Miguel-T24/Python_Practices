# 271. 270. Write a Python program to check if the elements of the first list are contained in the second one regardless of order.

def first_contained_second(l1,l2):
    for i in l1:
        if(i not in l2):
            return False
    return True

print(first_contained_second([1, 2], [2, 4, 1]))
print(first_contained_second([1], [2, 4, 1]))
print(first_contained_second([1, 1], [4, 2]))
print(first_contained_second([1, 1], [3, 2, 4, 1, 5, 1]))