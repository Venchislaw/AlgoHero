class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, val, root):
        if not root:
            return False
        else:
            if val < root.val:
                return self.search(val, root.left)
            elif val > root.val:
                return self.search(val, root.right)
            else:
                return True

    def insert(self, val, root):
        if not root:
            return Node(val)
        else:
            if val < root.val:
                root.left = self.insert(val, root.left)
            elif val > root.val:
                root.right = self.insert(val, root.right)

        return root

    def min_node(self, root):
        curr = root

        while curr.left:
            curr = curr.left
        return curr

    def remove(self, val, root):
        if not root:
            return None

        else:
            if val < root.val:
                root.left = self.remove(val, root.left)
            elif val > root.val:
                root.right = self.remove(val, root.right)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    min_node = self.min_node(root.right)
                    root.val = min_node.val

                    root.right = self.remove(min_node.val, root.right)

        return root

    def inorder_traverse(self, root):
        if not root:
            return None

        self.inorder_traverse(root.left)
        print(root.val)
        self.inorder_traverse(root.right)

    def preorder_traverse(self, root):
        if not root:
            return None

        print(root.val)
        self.inorder_traverse(root.left)
        self.inorder_traverse(root.right)

    def postorder_traverse(self, root):
        if not root:
            return None

        self.inorder_traverse(root.left)
        self.inorder_traverse(root.right)
        print(root.val)

    def tree_maze(self, leaf_val, root):
        if not root or root.val == 0:
            return False
        elif root.val == leaf_val:
            return True

        self.tree_maze(leaf_val, root.left)
        self.tree_maze(leaf_val, root.right)

        return False

    def can_reach_leaf(self, root):
        if not root or root.val == 0:
            return False

        if not root.left and not root.right:
            return True
        if self.can_reach_leaf(root.left):
            return True
        elif self.can_reach_leaf(root.right):
            return True

        return False


root = Node(3)
tree = Tree(root)

for i in range(100):
    tree.insert(i, root)

tree.insert(-2, root)
print(tree.tree_maze(-2, root))
print(tree.can_reach_leaf(root))
"""
print(tree.search(86, root))
print(tree.root.right.right.right.right.val)

tree.remove(1, root)
print(tree.search(1, root))

root = Node(5)
tree = Tree(root)
tree.insert(2, root)
tree.insert(1, root)
tree.insert(3, root)
tree.insert(7, root)
tree.insert(8, root)
tree.insert(6, root)

tree.remove(7, root)

print(tree.search(7, root))

tree.inorder_traverse(root)
print("----------")
tree.preorder_traverse(root)
print("----------")
tree.postorder_traverse(root)
"""