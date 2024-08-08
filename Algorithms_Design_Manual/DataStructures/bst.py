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
            
    def min_node(self, root):
        while root.left:
            root = root.left
        return root
        
    def max_node(self, root):
        while root.right:
            root = root.right
        return root
            
    def remove(self, root, val):
        if not root:
            return None
        
        if val < root.val:
            root.left = self.remove(root.left, val)
            if root.left:
                root.left.parent = root
        elif val > root.val:
            root.right = self.remove(root.right, val)
            if root.right:
                root.right.parent = root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_r_node = self.min_node(root.right)
                self.val = min_r_node.val
                self.remove(root.right, min_r_node)
                
        return root    
    
root = TreeNode(3)

tree = BST(root)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.print_out(root)
print(root.left.parent is root)  # True
tree.remove(root, 2)
tree.print_out(root)
print(root.left.parent is root)  # True
