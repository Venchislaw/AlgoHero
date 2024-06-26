class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, val, root):
        if val < root.val:
            if not root.left:
                root.left = Node(val)
            else:
                self.insert(val, root.left)

        elif val > root.val:
            if not root.right:
                root.right = Node(val)
            else:
                self.insert(val, root.right)

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
tree.insert(6, root)

print(tree.binary_search(6, root))  # True
print(tree.root.right.right.val)

