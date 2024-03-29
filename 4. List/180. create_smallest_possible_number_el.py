# 180. Write a Python program to create the smallest possible number using the elements of a given list of positive integers.

def create_largest_number(lst):
    if all(val == 0 for val in lst):
        return '0'
    result = ''.join(sorted((str(val) for val in lst), reverse=False,
                      key=lambda i: i*( len(str(min(lst))) * 2 // len(i))))
    return result


nums = [3, 40, 41, 43, 74, 9]
print("Original list:")
print(nums)
print("Smallest possible number using the elements of the said list of positive integers:")
print(create_largest_number(nums))