# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.inorder(root)
        return result[k-1]
    def inorder(self,root):
        if root is None:
            return []
        return (self.inorder(root.left)+[root.val]+self.inorder(root.right))