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

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            current = self.root
            
            while True:
                if val < current.val:
                    if not current.left:
                        current.left = TreeNode(val)
                        current.left.parent = current
                        break
                    current = current.left
                
                elif val > current.val:
                    if not current.right:
                        current.right = TreeNode(val)
                        current.parent = current
                        break
                    current = current.right
                
                else:
                    break
                
    def print_out(self, root):
        if root:
            self.print_out(root.left)
            print(root.val)
            self.print_out(root.right)
        

root = TreeNode(2)

tree = BST(root)
tree.insert(1)
tree.insert(3)
tree.print_out(root)
print(root.left.parent is root)  # True
