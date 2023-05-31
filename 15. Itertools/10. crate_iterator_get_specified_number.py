# 10. Write a python program to crate an iterator to get a specified number of permutations of elemets

import itertools as it
def permutations_data(iter, length):
    return it.permutations(iter, length)
#List
result = permutations_data(['A','B','C','D'], 3)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)