# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left) 
            return root
        # if root is None:
        #     return None
        # root.left = self.invertTree(root.left)
        # root.right = self.invertTree(root.right)
        # if root.left and root.right:
        #     root.left , root.right = root.right, root.left
        # elif root.left:
        #     root.right = root.left
        #     root.left = None
        # elif root.right:
        #     root.left = root.right
        #     root.right = None
        # return root