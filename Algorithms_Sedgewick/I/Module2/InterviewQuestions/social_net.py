"""
We are given n people in our social network and file with m timestams, where each timestamp represents the moment
when person a submitted a friendship with user b. We need to find the first timestamp when all the users are connect
(not directly, but through connections like "friend of a friend of a friend...").
We should do it in O(m log n) time using n additional space in memory.
"""

# Solution 1.
"""
Okay, it's easy if we use quick-union for this problem.
Each timestamp in our file is mapped to the "union()" operation.
Our Union-find is represented as an array of roots, so connection between all users means the same root for all of them
(see MODULE2/quick_union.py or MODULE2/quick_union_improved.py)

We go through all timestamps in O(m) and connect users using union() method in O(log_2 n).
Bam! O(m*log_2 n). What about memory complexity?
It's simple, we use Weighted Quick Union, so we store our users in "roots" array, which represents our connections in a tree-like
structure. We can also save tree_size, as it also takes O(n).
Our final memory complexity is O(2n), but we neglect constant and get O(n), which is our restriction.
Let's Code!
"""

class WeightedQuickUnion:
    def __init__(self, N) -> None:
        self.tree_sizes = [1 for _ in range(N)]
        self.roots = [i for i in range(N)]

    def root(self, i) -> int:
        while self.roots[i] != i:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        
        return i

    def union(self, p, q) -> None:
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p == root_q:
            return
        
        if self.tree_sizes[root_p] < self.tree_sizes[root_q]:
            self.roots[root_p] = root_q
            self.tree_sizes[root_q] += self.tree_sizes[root_p]
        else:
            self.roots[root_q] = root_p
            self.tree_sizes[root_p] += self.tree_sizes[root_q]

    def connected(self, p, q):
        return self.root(p) == self.root(q)


with open("InterviewQuestions/time_stamps.txt") as f:
    connected = False
    qu = WeightedQuickUnion(5)
    for line in f.readlines():
        line = line.replace("\n", "")
        time, p, q = line.split()
        qu.union(int(p), int(q))
        if len(set(qu.roots)) == 1:
            print(time)
            connected = True
            break
    
if not connected:
    print("Users didn't connect")
    print(qu.roots)
