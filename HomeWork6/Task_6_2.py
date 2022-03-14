from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


tree = Node(1)
tree.right = Node(3)
tree.left = Node(2)
tree.left.next = tree.right
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.left.next = tree.left.right
tree.right.right = Node(7)
tree.left.right.next = tree.right.right


def connect(root):
    if root is None or root.right is None:
        return root

    q = deque()
    q.append(root)

    while q:
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            if i != size - 1:
                curr.next = q[0]
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return root

