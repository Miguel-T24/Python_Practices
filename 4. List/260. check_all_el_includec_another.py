# 260. Write a Python program to check if all the elements of a list are included in another given list.

def list_included_another(l1,l2):
    for x in l2:
        if x not in l1:
            return False
    return True

print(list_included_another([10, 20, 30, 40, 50, 60], [20, 40]))
print(list_included_another([10, 20, 30, 40, 50, 60], [20, 80]))