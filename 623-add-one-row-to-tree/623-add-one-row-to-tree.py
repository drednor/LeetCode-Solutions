# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
        stack = [(root,1)]
        while stack:
            node,d = stack.pop()
            #print(node.val,d)
            if d == depth - 1:
                nodel = TreeNode(val, node.left,None)
                noder = TreeNode(val, None, node.right)
                node.left = nodel
                node.right = noder
            if node.right:
                stack.append((node.right,d+1))
            if node.left:
                stack.append((node.left,d+1))
            
        return root