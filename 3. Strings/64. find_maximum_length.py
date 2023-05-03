# 64. Write a ptyhon program to find the maximum length of consecutive 0's in a given binary string

def max_length_zeros(binary):
    return max(map(len,binary.split("1")))

print(max_length_zeros("111000010000110")) 