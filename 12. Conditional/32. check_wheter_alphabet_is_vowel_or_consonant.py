# 32. Write a ptyhon program to check whetehr an alphabet is vowel or consolant

def vow_cons(letter):
    return ("Is consonant", "Is Vowel")[letter.lower() in "aeiou" ]

print(vow_cons("k"))
print(vow_cons("a"))
print(vow_cons("B"))
print(vow_cons("E"))