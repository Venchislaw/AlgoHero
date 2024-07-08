class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        return self

    def pop(self):
        popped = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1

        while i * 2 < len(self.heap) - 1:
            if (i * 2 + 1 < len(self.heap)
                    and self.heap[i * 2 + 1] < self.heap[i * 2]
                    and self.heap[i * 2 + 1] < self.heap[i]):

                self.heap[i * 2 + 1], self.heap[i] = self.heap[i], self.heap[i * 2 + 1]
                i = i * 2 + 1

            elif self.heap[i * 2] < self.heap[i]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2

            else:
                break

        return popped

    def heapify(self, array):
        array.append(array[0])
        self.heap = array

        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur

            while i * 2 < len(self.heap) - 1:
                if (i * 2 + 1 < len(self.heap)
                        and self.heap[i * 2 + 1] < self.heap[i * 2]
                        and self.heap[i * 2 + 1] < self.heap[i]):

                    self.heap[i * 2 + 1], self.heap[i] = self.heap[i], self.heap[i * 2 + 1]
                    i = i * 2 + 1

                elif self.heap[i * 2] < self.heap[i]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i = i * 2

                else:
                    break
            cur -= 1

        return self.heap


heap = Heap()
heap.push(16)
heap.push(19)
heap.push(19)
heap.push(21)
heap.push(26)
heap.push(30)
heap.push(68)
heap.push(65)

print(heap.heap)

print("--------------")
print(heap.pop())

print(heap.heap)

heap.heapify([65, 68, 30, 16, 19, 19, 26, 21])
print(heap.heap)
