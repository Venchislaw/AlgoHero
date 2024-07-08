# building hashmap from scratch!

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Hashmap:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.map = [None] * self.capacity
        self.size = 0  # size variable will count filled nodes
        # while capacity counts all nodes

    def hash(self, key):
        hashed = 0
        for char in key:
            hashed += ord(char)

        return hashed % self.capacity

    def insert(self, key, val):
        i = self.hash(key)

        while True:
            if self.map[i] == None:
                self.map[i] = Pair(key, val)
                self.size += 1

                if self.size == self.capacity // 2:
                    self.rehash()
                return

            elif self.map[i].key == key:
                self.map[i].val = val
                return

            i += 1
            i = i % self.capacity

    def get(self, key):
        i = self.hash(key)

        while self.map[i] is not None:
            i += 1
            i = i % self.capacity

        return self.map[i]

    def rehash(self):
        self.capacity *= 2
        new_map = [None] * self.capacity
        old_map = self.map
        self.map = new_map
        self.size = 0

        for pair in old_map:
            if pair:
                self.insert(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print([pair.key, pair.val])


hash_map = Hashmap()
hash_map.insert("Hello", "World")
hash_map.insert("F", "Society")
hash_map.insert("WD", "F?")
hash_map.insert("WD", "F")

hash_map.print()
