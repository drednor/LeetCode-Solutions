# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxv):
            if node is None:
                return 0
            res = 1 if node.val >= maxv else 0
            maxv = max(node.val, maxv)
            res+=dfs(node.left,maxv)
            res+=dfs(node.right,maxv)
            return res
        return dfs(root,root.val)