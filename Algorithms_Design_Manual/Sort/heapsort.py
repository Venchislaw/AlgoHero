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
    

def heapify(arr):
    arr = [0] + arr
    n = len(arr) // 2
    
    while n > 0:
        i = n
        
        while i * 2 < len(arr):
            left = i * 2
            right = left + 1
            
            if right < len(arr) and arr[right] < arr[left] and arr[right] < arr[i]:
                arr[i], arr[right] = arr[right], arr[i]
                i = right

            elif arr[left] < arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                break
        
        n -= 1
    
    heap = Heap()
    heap.heap = arr
    return heap
            
            

# print(heapify([5, 4, 6, 2, 1]))


def heap_sort(arr):
    heap = heapify(arr)
    print(heap.heap)
    for i in range(len(arr)):
        arr[i] = heap.pop()
    return arr

print(heap_sort([5, 4, 8, 1, 2]))
