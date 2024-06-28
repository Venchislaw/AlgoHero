class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, val, root):
        if not root:
            return Node(val)

        elif val < root.val:
            root.left = self.insert(val, root.left)
        else:
            root.right = self.insert(val, root.right)

        return root

    def min_value_node(self, root):
        cur = root

        while cur.left:
            cur = cur.left
        return cur

    def binary_search(self, val, root):
        if not root:
            return False

        if val < root.val:
            return self.binary_search(val, root.left)
        elif val > root.val:
            return self.binary_search(val, root.right)
        else:
            return True

    def remove_node(self, val, root):
        # In case we didn't find node
        if not root:
            return None

        elif val < root.val:
            root.left = self.remove_node(val, root.left)
        elif val > root.val:
            root.right = self.remove_node(val, root.right)
        # In case we found
        else:
            # Main removal logic:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                min_node = self.min_value_node(root.right)
                root.val = min_node.val

                self.remove_node(min_node.val, root.right)



root = Node(4, Node(2), Node(5))
tree = BinaryTree(root)
tree.insert(6, root)

tree.remove_node(6, root)
print(tree.binary_search(6, root))
