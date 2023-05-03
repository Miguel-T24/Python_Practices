# 62. Write a ptyhon program to compute the sum of the digits in a given string

def compute_sum_digit(string):
    return sum(map(lambda x:int(x), list(filter(lambda x:x.isdigit(), string))))

print(compute_sum_digit("jcnjkew123kjfd556"))
