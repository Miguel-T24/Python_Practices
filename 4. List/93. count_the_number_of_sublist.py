# 93. Write a python program to count the number of sublists that contain a particular element

def count_sublist(lista, num):
    return sum(map(lambda x:num in x,lista))

print(count_sublist([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
print(count_sublist([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 7))
print(count_sublist([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], "A"))
print(count_sublist([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], "E"))