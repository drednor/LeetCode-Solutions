# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res = []
        temp = []
        stack =[(root, targetSum - root.val, temp + [root.val])]
        while stack:
            cur, target, check = stack.pop()
            temp.append(cur.val)
            if not cur.left and not cur.right and target == 0:
                    res.append(check)
            if cur.right:
                stack.append((cur.right, target-cur.right.val, check + [cur.right.val]))
            if cur.left:
                stack.append((cur.left, target-cur.left.val, check + [cur.left.val]))
        return res
    
                
        
        
        
        # res = []
        # def dfs(node, temp, target):
        #     if not node:
        #         return
        #     temp.append(node.val)
        #     target -= node.val
        #     if node.right == None and node.left == None:
        #         if target == 0:
        #             res.append(temp.copy())
        #     else:
        #         dfs(node.left, temp,target)
        #         dfs(node.right, temp, target)
        #     temp.pop()
        #     return 
        # dfs(root, [], targetSum)
        # return res
            
        
        