class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        cur = self.root

        while cur.left or cur.right:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right

        if val < cur.val:
            cur.left = Node(val)
        else:
            cur.right = Node(val)

        return self

    def binary_search(self, val, root):
        if not root:
            return False

        if val < root.val:
            return self.binary_search(val, root.left)
        elif val > root.val:
            return self.binary_search(val, root.right)
        else:
            return True


root = Node(4, Node(2), Node(5))
tree = BinaryTree(root)
tree.insert(6)

print(tree.binary_search(6, root))  # True
print(tree.root.right.right.val)

