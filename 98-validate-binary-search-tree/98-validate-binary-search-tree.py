# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if node is None:
                return True
            if not(node.val > left and node.val< right):
                return False
            return valid(node.left,left,node.val) and valid(node.right, node.val , right)
        return valid(root, float("-inf"), float("inf"))
#         if root is None:
#             return True
#         result = self.traverse_in_order(root)
#         if result == sorted(result):
#             return True
#         else:
#             return False

    
#     def traverse_in_order(self, root):
#         if root is None:
#             return []
#         return (self.traverse_in_order(root.left) +[root.val] + self.traverse_in_order(root.right))