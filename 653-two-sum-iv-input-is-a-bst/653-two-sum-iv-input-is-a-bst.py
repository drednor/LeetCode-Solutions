# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        memo = {}
        memo[k-root.val] = 1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                if node.right.val in memo:
                    return True
                else:
                    stack.append(node.right)
                    memo[k-node.right.val] = 1
            if node.left:
                if node.left.val in memo:
                    return True
                else:
                    stack.append(node.left)
                    memo[k-node.left.val] = 1
        return False