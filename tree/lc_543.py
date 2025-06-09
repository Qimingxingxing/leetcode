# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            ll, ld = dfs(node.left)
            rl, rd = dfs(node.right)
            return max(ld + rd + 1, ll, rl), max(ld, rd) + 1

        return dfs(root)[0] - 1
