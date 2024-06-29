def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return None

    print(root.val)
    inorder(root.left)
    inorder(root.right)


def postorder(root):
    if not root:
        return None

    inorder(root.left)
    inorder(root.right)
    print(root.val)
