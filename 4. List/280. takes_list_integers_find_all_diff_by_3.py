# 280. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list.

def find_all_diff_3(l):
    r = []
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(abs(l[i]-l[j]) == 3):
                r.append([l[i],l[j]])
    return r

print([0, 3, 4, 7, 9])
print(find_all_diff_3([0, 3, 4, 7, 9]))
print()
print([0, -3, -5, -7, -8] )
print(find_all_diff_3([0, -3, -5, -7, -8] ))
print()
print([1, 2, 3, 4, 5])
print(find_all_diff_3([1, 2, 3, 4, 5]))
print()
print([100, 102, 103, 114, 115])
print(find_all_diff_3([100, 102, 103, 114, 115]))