class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)


def lowestCommonAncestor(root, p, q):
    tree_roots = {}

    def helper(some_root, ans):
        if some_root:
            ans.append(some_root.val)
            helper(some_root.left, ans)
            helper(some_root.right, ans)
        return ans

    def checker(root):
        if root:
            curr_root = []
            tree_roots[root.val] = helper(root, curr_root)
            checker(root.left)
            checker(root.right)

    checker(root)

    idx = root.val
    children = tree_roots[root.val]

    for key in tree_roots:
        if p in tree_roots[key] and q in tree_roots[key] and len(children) > len(tree_roots[key]):
            idx = key
            children = tree_roots[key]

    return idx


print(lowestCommonAncestor(tree, 5, 4))
