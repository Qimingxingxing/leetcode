"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque([root])
        while q:
            l = len(q)
            temp = []
            for _ in range(l):
                cur = q.popleft()
                temp.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            for i, node in enumerate(temp):
                if i == len(temp)-1:
                    node.next = None
                else:
                    node.next = temp[i+1]
        return root
