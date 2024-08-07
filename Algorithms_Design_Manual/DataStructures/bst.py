class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BST:
    def __init__(self, root):
        self.root = root
        
    def search(self, root, val):
        if not root:
            return None
        
        elif val > root.val:
            return self.search(root.right, val)
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return root

left = TreeNode(1)
right = TreeNode(3)
root = TreeNode(2, left=left, right=right)
left.parent = root; right.parent = root


tree = BST(root)
print(tree.search(root, left.val))
