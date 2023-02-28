#  26. write a python program to create a histogram from given list of integers
 
def histogram(nums):
    for i in range (len(nums)):
        for it in range(nums[i]):
            print("*",end="")
        print(end = "\n")

histogram([2,3,4,6,5])