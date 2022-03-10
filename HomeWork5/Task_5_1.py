
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(3)


def post_order(root):
    ans = []

    def foo(node):
        if node:
            foo(node.left)
            foo(node.right)
            ans.append(node.val)
    foo(root)
    return ans


print(post_order(tree))