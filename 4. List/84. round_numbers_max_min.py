# 84. Write a python program to round the numbers on a given list, print the minimum and maximum numbers and multiply the numbers by 5. print the unique numbers in ascending order separated by space.

lista = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

list_rounded  = list(map(lambda x:round(x),lista))
print("List Rounded:\n{}".format(list_rounded))
print("Maximum:\n{}".format(max(list_rounded)))
print("Minimum:\n{}".format(min(list_rounded)))
print("Result in ascending order:\n",*sorted(list_rounded))


