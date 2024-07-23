# oke. Let's start with search
# it's only one algo

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return None


print("binary search: ", binary_search([1, 3, 5, 7, 9], 5))

# sorting. Hehe boi...


def get_min_idx(arr):
    min_val = arr[0]
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    return min_idx

def selection_sort(arr):
    new_arr = []

    while len(arr) > 0:
        min_idx = get_min_idx(arr)
        new_arr.append(arr.pop(min_idx))

    return new_arr


print("selection sort: ", selection_sort([2, 5, 7, 1, 4]))


def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i

        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

print("insertion sort: ", insertion_sort([2, 5, 7, 1, 4]))


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr if i > pivot]

    return qsort(less) + [pivot] + qsort(more)

print("quick sort: ", qsort([2, 5, 7, 1, 4]))

# alright... It's gonna be a litle challenge

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # merge starts here

        min_l = 0
        min_r = 0
        i = 0

        while min_l < len(left_half) and min_r < len(right_half):
            if left_half[min_l] < right_half[min_r]:
                arr[i] = left_half[min_l]
                min_l += 1
            else:
                arr[i] = right_half[min_r]
                min_r += 1
            i += 1

        # residuals while loops

        while min_l < len(left_half):
            arr[i] = left_half[min_l]
            min_l += 1
            i += 1
        
        while min_r < len(right_half):
            arr[i] = right_half[min_r]
            min_r += 1
            i += 1

    return arr


print("merge sort: ", merge_sort([2, 1, 4, 5, 7]))


def bucket_sort(arr):
    buckets = [0] * (max(arr) + 1)

    for number in arr:
        buckets[number] += 1

    j = 0
    for i in range(len(buckets)):
        for _ in range(buckets[i]):
            arr[j] = i
            j += 1
    return arr

print("bucket sort: ", bucket_sort([2, 1, 4, 5, 7]))


# we're done with sorting, searching and stuff...
# Now it's time for the real deal... DataStructures


# Dynamic Arrays:
print(f"{'-'*60}\n DATA STRUCTURES \n {'-'*60}")
dynamic_arr = ["It's", "Too", "Easy"]
print("Dynamic Array: ", dynamic_arr)

# HashSet/Hashmap:

# built-in:

set_ = set(["Hello", "mom!"])
print("built-in set: ", set_)

hash_map = {"Hello": "Mom", "I'm on": "MTV!"}
print("built-in hashmap: ", hash_map)

# from scratch:

class HashSet:
    def __init__(self, capacity=2) -> None:
        self.set = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def hash(self, val) -> int:
        key = val % self.capacity
        return key
    
    def add(self, val) -> None:
        key = self.hash(val)

        if self.set[key]:
            self.set[key] = val
        else:
            self.set[key] = val
            self.size += 1
            
            if self.size >= len(self.set) * 0.5:
                self.rehash()


    def includes(self, val) -> bool:
        key = self.hash(val)
        return self.set[key] is not None


    def remove(self, val) -> None:
        if self.includes(val):
            key = self.hash(val)
            self.set[key] = None
        

    def rehash(self) -> None:
        old_set = self.set
        self.capacity *= 2
        self.size = 0
        self.set = [None] * self.capacity

        for val in old_set:
            if val:
                self.add(val)

print("Hashset from scratch test: ")
hashset = HashSet()
hashset.add(2)
hashset.add(3)
hashset.add(5)
hashset.remove(2)
print(hashset.set)
print(hashset.includes(3))
print(hashset.includes(4))
print("Hashset tests are over")


print("Hashmap From Scratch: ")


class Pair:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val


class Hashmap:
    def __init__(self, capacity=2) -> None:
        self.capacity = capacity
        self.map = [None] * capacity
        self.size = 0

    def hash(self, key) -> int:
        return key % self.capacity

    def add(self, key, val) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1

                if self.size >= self.capacity * 0.5:
                    self.rehash()
                return
            
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            index += 1
            index = index % self.capacity

    def get(self, key):
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                return None
            
            elif self.map[index].key == key:
                return self.map[index].val
            
            index += 1
            index = index % self.capacity

    def remove(self, key) -> None:
        if not self.get(key):
            return None
        
        index = self.hash(key)

        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            
            index += 1
            index = index % self.capacity

    def rehash(self) -> None:
        old_map = self.map
        self.capacity *= 2
        self.size = 0

        self.map = [None] * self.capacity

        for pair in old_map:
            if pair:
                self.add(pair.key, pair.val)


hmap = Hashmap()
hmap.add(1, 2)
hmap.add(2, 3)
print(hmap.map)
print(hmap.get(1))
print(hmap.get(0))
hmap.remove(1)
print(hmap.map)
print(hmap.get(1))

print("End of HashMap from scratch")


# Linked Lists


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head

    def add(self, val):
        cur = self.head
        
        while cur.next:
            cur = cur.next
        
        cur.next = Node(val, None)

    def print(self):
        cur = self.head

        while cur:
            print(cur.val)
            cur = cur.next

    def remove(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        
        cur = self.head.next
        cur_prev = self.head

        while cur:
            if cur.val == val:
                cur_prev.next = cur.next
                return
            
            cur_prev = cur
            cur = cur.next

print("Linked List experiments:")
ll = LinkedList(Node(1))
ll.add(2)
ll.add(3)

ll.print()

print("_--------------")

ll.remove(3)
ll.add(5)
ll.print()
print("-----")
ll.remove(1)
ll.print()
print("-----")
ll.remove(2)
ll.print()

# Umom!

print("Linked List experiments are over")



# T R E E S


