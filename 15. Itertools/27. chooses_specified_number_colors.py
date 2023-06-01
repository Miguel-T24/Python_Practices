# 27. crate a python porgram that chooses a specified number of colors form three different colors and generate unique combinations

from itertools import combinations 
def unique_combinations_colors(list_data, n):
    return [" and ".join(items) for items in combinations(list_data, r=n)]
colors = ["Red","Green","Blue"]
print("Original List: ",colors)
n=1
print("\nn = 1")
print(list(unique_combinations_colors(colors, n)))
n=2
print("\nn = 2")
print(list(unique_combinations_colors(colors, n)))
n=3
print("\nn = 3")
print(list(unique_combinations_colors(colors, n)))