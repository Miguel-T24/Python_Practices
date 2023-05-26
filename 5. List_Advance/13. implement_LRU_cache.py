# 13. Write a python function to implement LRU cache

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)

cache.put(10, 10)
cache.put(20, 20)
print(cache.get(10))   #10
cache.put(30, 30)       
print(cache.get(20))   #-1 
cache.put(40, 40)      
print(cache.get(10))   #-1 
print(cache.get(30))   #30
print(cache.get(40))   #40