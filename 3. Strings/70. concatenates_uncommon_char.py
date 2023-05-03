# 70. Write a python program that concatenates uncommon characters from two strings

def concat_uncommon(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    concat = []
    concat.append("".join(list(filter(lambda x:x not in s2, s1))))
    concat.append("".join(list(filter(lambda x:x not in s1, s2))))

    return "".join(concat)

s1 = 'abcdpqr'
s2 = 'xyzabcd'


print("Originals: \n{}\n{}".format(s1,s2))
print("Uncommon: {}".format(concat_uncommon(s1,s2)))

