# 22. Write a python program that finds all pairs of elements in a lists whose sum is a euqal to a given value

def find_pairs(nums, target_val):
    nums_set = set(nums)
    pairs = []
    for n in nums_set:
        complement = target_val - n
        if complement in nums_set:
            pairs.append({n, complement})
    return pairs

lista = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Original: {}".format(lista))
print("target: 35")
print("Pairs: {}".format(find_pairs(lista,35)))
