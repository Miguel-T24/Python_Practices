# 83. Write a python program to round every number in a given list of numbers and rprint the total sum multiplied by the length of the list

lista = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

result = list(map(lambda x:round(x),lista))

print("List Rounded:\n{}".format(result))
print("sum and multiply by the length of the sum:\n{}".format(sum(result)*len(result)))
