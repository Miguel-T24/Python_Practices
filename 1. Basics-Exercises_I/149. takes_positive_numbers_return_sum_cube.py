# 149. Write a python function that tkaes  aposotive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def sum_integer_smaller_number(n):
    # sum = 0
    # for i in [x for x in range(1, n)]:
    #     if i > 0 and  i < n:
    #         sum += pow(i,3)
    # return sum

    return sum([pow(x,3) for x in range(1,n)])


print(sum_integer_smaller_number(8))