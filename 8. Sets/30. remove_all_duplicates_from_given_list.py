# 30. Write a python program to remove all duplicates from a given lists of strings and return a list of unique strnigs. Use the python set data type.

strings = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
print("Original: {}".format(strings))
print("Unique  : {}".format(list(set(strings))))
