# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def dfs(node,total):
            if node is None:
                return False
            total += node.val
            if not node.left and not node.right and total == targetSum:
                return True
            return dfs(node.left, total) or dfs(node.right, total)
        return dfs(root,0)