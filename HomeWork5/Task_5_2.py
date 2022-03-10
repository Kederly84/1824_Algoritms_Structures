class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(2)
tree.right.right = TreeNode(3)
tree.left.left = TreeNode(3)
tree.right.left = TreeNode(4)
tree.left.right = TreeNode(4)


def checker(root):
    def foo(node_left, node_right):
        if not node_left and not node_right:
            return True
        if node_left and node_right and node_left.val == node_right.val:
            return foo(node_left.left, node_right.right) and foo(node_left.right, node_right.left)
        else:
            return False

    if root:
        return foo(root.left, root.right)
    else:
        return False


print(checker(tree))
