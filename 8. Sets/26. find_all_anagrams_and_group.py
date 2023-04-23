# 26. write a ptyhon program to find all the anagrams and group them together from a given list of strings. Use the Python data type

def group_anagrams(strs):
    result = {}
    for s in strs:
        sorted_string = ''.join(sorted(s))
        if sorted_string in result:
            result[sorted_string].append(s)
        else:
            result[sorted_string] = [s]
    return list(result.values())

strs = ['eat', 'cba', 'tae', 'abc', 'xyz']
print("Original list of strings:") 
print(strs)
print("Find and group all anagrams in the said list:")
print(group_anagrams(strs))
strs = ['restful','forty five','evil','over fifty','vile','fluster']
print("\nOriginal list of strings:") 
print(strs)
print("Find and group all anagrams in the said list:")
print(group_anagrams(strs))