# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, cur):
            if not node:
                return
            cur = node.val + cur * 10
            if not node.left and not node.right:
                self.res += cur
                return
            dfs(node.left, cur)
            dfs(node.right, cur)

        self.res = 0
        dfs(root, 0)
        return self.res