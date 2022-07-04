# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        def dfs(root):
            if root is None:
                return 0
            #print("root.val = ", root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            # print("left = ",left)
            # print("right = ",right)
            if abs(left-right)>1:
                flag[0] = False
            return 1+max(right,left)
        dfs(root)
        #print(ans)
        return flag[0]
        