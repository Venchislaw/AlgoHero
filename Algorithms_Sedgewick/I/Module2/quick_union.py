"""
QuickUnion is a solution to the union-find. It performs 2 main methods:
union - connects 2 points
connected - checks whether 2 points are connected (not necessarily directly).
QuickFind is relatively slow, so we want a better solution.

This data structure stores root value at self.roots[i] of i value i.
For example, if we have a value of 5 with root 3 it means we have a 5th element in self.roots = 3
self.roots[5] = 3.

Each method uses helper method root(i), which finds root of i. It returns us value, for situation described above:
root(5) = 3
"""



class QuickUnion:
    def __init__(self, N) -> None:
        self.roots = [i for i in range(N)]
    
    # returns root index of the element i
    def root(self, i) -> int:
        while self.roots[i] != i:
            i = self.roots[i]
        return i
    
    def union(self, p, q) -> None:
        root_p = self.root(p)
        root_q = self.root(q)

        self.roots[root_p] = root_q

    def connected(self, p, q) -> bool:
        return self.root(p) == self.root(q)

# Same test cases as for QuickFind

qckunion = QuickUnion(10)
qckunion.union(0, 5)
qckunion.union(6, 5)
qckunion.union(1, 2)
qckunion.union(7, 2)
qckunion.union(8, 3)
qckunion.union(3, 4)
qckunion.union(4, 9)

print(qckunion.connected(0, 6))  # expected: True; output: True
print(qckunion.roots)  # [5, 2, 2, 4, 9, 5, 5, 2, 3, 9]


# However even this implementation is not good enough
# As our tree can be skinny and imbalanced, so connected() operation will take O(n)
# Bruh...
