# 70. Write a python program to map the values of a gievn list to a dictionary using a function, where the key-value pairs consist of the original valuue as the key and th eresult of the function as the value

def test(itr, fn):
  return dict(zip(itr, map(fn, itr)))
print(test([1, 2, 3, 4], lambda x: x * x))