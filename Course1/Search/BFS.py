from collections import deque
from Course1.DataStructures.binary_tree import tree


def breadth_first_search(root):
    queue = deque()

    level = 0
    queue.append(root)
    while len(queue) > 0:
        print(f"Level {level}\n{'-' * 60}")
        for _ in range(len(queue)):
            cur = queue.popleft()
            print(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print("-" * 60)
        level += 1


breadth_first_search(tree.root)
