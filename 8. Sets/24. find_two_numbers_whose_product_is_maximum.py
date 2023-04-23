# 24. Write a ptyhon program to find the two numbers whose product is maximum among all the pais in a given lists of numbers. use python set

def max_product(nums):
    nums_set = set(nums)
    max_product = float('-inf')
    max_num1 = None
    max_num2 = None
    for n1 in nums_set:
        for n2 in nums_set:
            if n1 != n2 and n1 * n2 > max_product:
                max_product = n1 * n2
                max_num1 = n1
                max_num2 = n2
    return (max_num1, max_num2)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list of integers:")
print(nums)
print("Maximum product of two numbers among all pairs in the said list:")
print(max_product(nums))