# 16. Write a python program to remove leading zeros from an ip address

from re import sub

def remove_leading_zeros(ip):
    return sub("\.0",".",ip)

print(remove_leading_zeros("216.08.094.196"))