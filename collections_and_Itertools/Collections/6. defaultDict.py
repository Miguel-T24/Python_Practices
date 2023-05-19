# defaultdict

print("Default Dict:")

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print('d:', d) # d: defaultdict(<function default_factory at 0x7f6e410d7b00>, {'foo': 'bar'})
print('foo =>', d['foo']) # bar
print('bar =>', d['bar']) # default value