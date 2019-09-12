"""
author: buppter
datetime: 2019/9/12 11:20
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.key = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.key.remove(key)
            self.key.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.key.remove(key)
            self.key.insert(0, key)
        else:
            if len(self.key) >= self.capacity:
                cur = self.key.pop()
                self.cache.pop(cur)

            self.key.insert(0, key)
            self.cache[key] = value


s = LRUCache(3)
s.put(2,1)
s.put(2,2)
print(s.get(2))
s.put(1,1)
s.put(4,1)
print(s.get(2))

