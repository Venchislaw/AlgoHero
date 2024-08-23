class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1

        while self.heap[i // 2] > self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2
        
    def pop(self):
        popped = self.heap[1]
        if len(self.heap) > 2:
            self.heap[1] = self.heap.pop()
        else:
            self.heap.pop()
            return popped
        i = 1

        while i * 2 < len(self.heap):
            left = i * 2
            right = left + 1

            if right < len(self.heap) and self.heap[right] < self.heap[left] and self.heap[right] < self.heap[i]:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right

            elif self.heap[left] < self.heap[i]:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            else:
                break
        return popped
    
    def __len__(self):
        return len(self.heap) - 1
    

def make_heap(arr):
    heap = Heap()
    for item in arr:
        heap.insert(item)
    return heap


def heap_sort(arr):
    heap = make_heap(arr)
    res = []
    while len(heap) > 0:
        res.append(heap.pop())
    return res

print(heap_sort([5, 4, 8, 1, 2]))