# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # stack = [(root,"")]
        # res = []
        # while stack:
        #     node , ls = stack.pop()
        #     if not node.right  and not node.left:
        #         res.append(ls + str(node.val))
        #     if node.right:
        #         stack.append((node.right, ls + str(node.val) + "->"))
        #     if node.left:
        #         stack.append((node.left, ls + str(node.val) + "->"))
        # return res
        res = []
        def dfs(node, temp):
            if not node:
                return 
            if not node.right and not node.left:
                res.append(temp + str(node.val))
            if node.right:
                dfs(node.right, temp + str(node.val) + "->")
            if node.left:
                dfs(node.left, temp + str(node.val) + "->")
            return
        dfs(root, "")
        return res
        