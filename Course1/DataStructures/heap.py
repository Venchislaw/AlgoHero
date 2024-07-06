class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while val < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        return self

    def pop(self):
        popped = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1

        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap)
                    and self.heap[i * 2 + 1] < self.heap[i * 2]
                    and self.heap[i * 2 + 1] < self.heap[i]
            ):
                self.heap[i * 2 + 1], self.heap[i] = self.heap[i], self.heap[i * 2 + 1]
                i = i * 2 + 1

            elif self.heap[i * 2] < self.heap[i]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i *= 2
            else:
                return popped

        # return popped


    def heapify(self, array):
        array.append(array[0])

        self.heap = array

        # we can skip half of array
        # as elems in it don't have any children
        cur = (len(array) - 1) // 2

        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and
                        self.heap[2 * i + 1] < self.heap[2 * i] and
                        self.heap[i] > self.heap[2 * i + 1]):

                    self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                    i = 2 * i
                else:
                    break
            cur -= 1


heap = Heap()
heap = heap.push(5)
heap = heap.push(3)
heap = heap.push(1)

print(heap.heap)
heap.pop()
print(heap.heap)
heap = heap.push(10)
heap.pop()
print(heap.heap)


heap.heapify([1, 2, 4, 6, 5])
print(heap.heap)
