"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return root
        stack = [root]
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(cur.children[::-1])
        return result
        
        
        # result = []
        # def recurse(root,result):
        #     if root:
        #         result.append(root.val)
        #         for child in root.children:
        #             recurse(child, result)
        #     return result
        # return recurse(root, [])
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # RECURSIVE SOULTIOn
        # def helper(root,result):
        #     if root:
        #         result.append(root.val)
        #         for child in root.children:
        #             helper(child, result)
        #     return result
        # return helper(root,[])
        
        # ITERATIVE SOLUTION
        # if root is None:
        #     return None
        # output = []
        # stack = [root]
        # while stack:
        #     temp = stack.pop()
        #     output.append(temp.val)
        #     stack.extend(temp.children[::-1])
        # return output
                
        
        
        