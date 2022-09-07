# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node is None:
                return ""
            s = str(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            if left == "" and right == "":
                return s
            elif left == "":
                s += "()" + "(" + right + ")"
            elif right == "":
                s += "("+ left + ")"
            else:
                s += "(" +  left  + ")" + "(" + right + ")"
            return s
            #return  str(node.val) + "(" + dfs(node.left) + ")"+ "(" + dfs(node.right) +")"
        return dfs(root)
#         print(res)
#         res = res.replace("()","")
#         return res
        
        