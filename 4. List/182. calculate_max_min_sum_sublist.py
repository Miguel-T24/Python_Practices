# 182. Write a python program to calculate the maximum and minimum sum of a sublist ina  given list of lists

l = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

maxi = max(list(map(lambda x:(x,sum(x)),l)),key=lambda x:x[1])
print(maxi[0])
mini = min(list(map(lambda x:(x,sum(x)),l)),key=lambda x:x[1])
print(mini[0])