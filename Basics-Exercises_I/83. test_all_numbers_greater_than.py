# 83. QWrite a python program to test whether all numbers in a list are greater than certain number

# def test(numbers, greater_than):
#     for i in numbers:
#         if(i <  greater_than):
#             return False
#     return True
            


# print(test([1,2,3] , 5))
# print(test([6,1,3] , 5))
# print(test([6,10,20] , 5))


# Best Solution
def test(numbers , greater_than):
    return all(x > greater_than for x in numbers)

print(test([1,2,3] , 5))
print(test([6,1,3] , 5))
print(test([6,10,20] , 5))
