# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            if node.val == 0 and left == False and right == False:
                return False
            return True
        flag = dfs(root)
        if not flag:
            root = None
        return root
        # def dfs(node):
        #     if node is None:
        #         return True
        #     if node.right is None and node.left is None:
        #         if node.val == 0:
        #             return False
        #         if node.val == 1:
        #             return True
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if not left:
        #         node.left = None
        #     if not right:
        #         node.right = None
        #     if node.val == 0 and :
        #         return False
        #     if node.val == 1:
        #         return True
        # dfs(root)
        # return root