# 13. Write a python program to count the even and odd numbers in a given array of integers using lambda

array = [1,2,3,5,7,8,9,10]

even = len(list(filter(lambda x:x%2==0, array)))
odd = len(list(filter(lambda x:x%2!=0,array)))

print("Original array:",array)
print("Number of Even :",even)
print("Number of Odds :",odd)
