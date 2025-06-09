# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, temp):
            if not node:
                return
            temp.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(temp))
            for child in (node.left, node.right):
                dfs(child, temp)
            temp.pop()
        res = []
        dfs(root, [])
        return res