# 13. Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.


from itertools import combinations

def comb_two_sig(dig):
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    r = string_maps[dig[0]] + string_maps[dig[1]]
    r = list(combinations(r,2))
    for i in r:
        print("".join(i), end=" ")
    print()
comb_two_sig('47')
comb_two_sig('29')
