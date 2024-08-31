"""
QuickFind is a solution to the union-find. It performs 2 main methods:
union - connects 2 points
connected - checks whether 2 points are connected (not necessarily directly).
"""


class QuickFind:
    def __init__(self, N):
        self.connections = [i for i in range(N)]
    
    def connected(self, p, q) -> bool:
        return self.connections[p] == self.connections[q]
    
    def union(self, p, q) -> None:
        p_id = self.connections[p]
        q_id = self.connections[q]

        for i in range(len(self.connections)):
            if self.connections[i] == p_id:
                self.connections[i] = q_id


qckfind = QuickFind(10)
qckfind.union(0, 5)
qckfind.union(6, 5)
qckfind.union(1, 2)
qckfind.union(7, 2)
qckfind.union(8, 3)
qckfind.union(3, 4)
qckfind.union(4, 9)

print(qckfind.connected(0, 6))  # expected: True; output: True
print(qckfind.connections)  # [5, 2, 2, 9, 9, 5, 5, 2, 9, 9]


# This solution is relatively simple, but sadly...
# Inefficient. Connected operation works perfectly well in O(1) time, while union takes O(n) time
# So, if we want to union n elements we will face time complexity O(n^2).
