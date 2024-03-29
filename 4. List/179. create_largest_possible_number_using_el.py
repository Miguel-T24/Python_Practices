# 179. Write a python program to ccreate the largest possible number usgin the elements of a given list of positive itegers

def create_largest_number(lst):
    if all(val == 0 for val in lst):
        return '0'
    result = ''.join(sorted((str(val) for val in lst), reverse=True,
                      key=lambda i: i*( len(str(max(lst))) * 2 // len(i))))
    return result
nums = [3, 40, 41, 43, 74, 9]
print("Original list:")
print(nums)
print("Largest possible number using the elements of the said list of positive integers:")
print(create_largest_number(nums))