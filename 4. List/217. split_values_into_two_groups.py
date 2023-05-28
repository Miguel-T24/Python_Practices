# 217. Write a python program to split values into two grups, based on the result of the given filteritng function

def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
print(bifurcate_by(['red', 'green', 'black', 'white'], lambda x: x[0] == 'w'))