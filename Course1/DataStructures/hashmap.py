class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity

    def hash(self, key):
        result = 0

        for char in key:
            result += ord(char)

        return result % self.capacity

    def insert(self, key, val):
        i = self.hash(key)

        while True:
            if self.map[i] is None:
                self.map[i] = Pair(key, val)
                self.size += 1

                if self.size >= self.capacity // 2:
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
            if self.map[i].key == key:
                return self.map[i].val
            i += 1
            i = i % self.capacity

        return None

    def rehash(self):
        self.capacity *= 2
        new_map = [None] * self.capacity

        old_map = self.map
        self.map = new_map

        for pair in old_map:
            if pair:
                self.insert(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print([pair.key, pair.val])

    def remove(self, key):
        if not self.get(key):
            return

        i = self.hash(key)
        while True:
            if self.map[i].key == key:
                self.map[i] = None
                self.size -= 1
                return
            i += 1
            i = i % self.capacity


hash_map = HashMap()
hash_map.insert("Hello", "World")
hash_map.insert("F", "Society")
hash_map.insert("WD", "F?")
hash_map.insert("WD", "F")


hash_map.remove("Hello")
hash_map.print()
