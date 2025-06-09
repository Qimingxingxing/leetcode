class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def verticalTraversal(self, root):
        cols = collections.defaultdict(list)
        q = deque([(root, 0)])
        while q:
            l = len(q)
            for _ in range(l):
                node, i = q.popleft()
                cols[i].append(node.val)
                if node.left:
                    q.append((node.left, i-1))
                if node.right:
                    q.append((node.right, i+1))
        return [cols[i] for i in sorted(cols.keys())]

# {
#     -1: [9],
#     0: [3, 15],
#     1: [20]
#     2: [7]
# }