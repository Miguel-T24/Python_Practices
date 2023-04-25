# 30. Write a ptyhon program to sort a given matrix in ascending order according to the sum of itrs rows using lambda

list1=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]

result = sorted(list1, key=lambda x:sum(x))

print(result)