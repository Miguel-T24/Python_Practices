# 23. Write a python program to find the longest commom prefix of all strings. Use the Python set

def longest_Common_Prefix(strs):
    if not strs:
        return ""
    min_length = min([len(word) for word in strs])
    for i in range(min_length):
        chars = set([word[i] for word in strs])
        if len(chars) > 1:
            return strs[0][:i]
    return strs[0][:min_length] 

strs = ["pqrefgh","pqrsfgh"]
print("Original list of strings:")
print(strs)
print("Longest common prefix of all said strings:")
print(longest_Common_Prefix(strs))