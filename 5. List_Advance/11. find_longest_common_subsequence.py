# 11. Write a python function fo find the longest common subsequence in two lists

def longest_common_subsequence(lst1, lst2):
    m, n = len(lst1), len(lst2)
    jh = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if lst1[i-1] == lst2[j-1]:
                jh[i][j] = 1 + jh[i-1][j-1]
            else:
                jh[i][j] = max(jh[i-1][j], jh[i][j-1])
    
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if lst1[i-1] == lst2[j-1]:
            result.append(lst1[i-1])
            i -= 1
            j -= 1
        elif jh[i-1][j] > jh[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return result[::-1]

nums1 =  [1,2,3,4,5,6,7,8]
nums2 =  [6,7,5,6,7,8]
print("Original lists:")
print(nums1)
print(nums2)
result = longest_common_subsequence(nums1,nums2)
print("Longest common sub-sequence in two lists:")
print(result)