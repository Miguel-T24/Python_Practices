# Python Set Operations

# Union Two Sets
print("1. Union Two Sets")
a = {1,2,3}
b = {4,5,6}

# two Ways
print("Way 1:",a|b)
print("Way2:",a.union(b))

# Intersection
print("\n2. Intersection")
a = {1,3,5}
b = {1,2,3}

# Two ways
print("Way 1:",a&b)
print("Way 2:",a.intersection(b))

# Difference Between two sets
print("\n3. Difference between two sets")
a = {2,3,5}
b = {1,2,6}

#Two Ways
print("Way 1:",a-b)
print("Way 2:",a.difference(b))

# Symmetric Difference
print("\n4. Symmetric Difference")
a = {2,3,4}
b = {1,2,6}

# Two Ways
print("Way 1:",a^b)
print("Way 1:",a.symmetric_difference(b))

# Check Two set are equal
print("\n5. Check if two sets are equal")
a = {1,3,5}
b = {3,5,1}

#Two Ways
print(a==b)

# update
print("\n6. Update")
a = {'a','b'}
b = {1,2,3}

a.update(b)
print(a)