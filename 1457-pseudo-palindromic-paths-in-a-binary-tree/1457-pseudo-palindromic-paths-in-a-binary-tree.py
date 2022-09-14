# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # stack = [(root, [])]
        # res = []
        # while stack:
        #     node, temp = stack.pop()
        #     if not node.right and not node.left:
        #         res.append(temp + [node.val])
        #     if node.right:
        #         stack.append((node.right, temp+[node.val]))
        #     if node.left:
        #         stack.append((node.left, temp+[node.val]))
        # return 2
        
        def dfs(node, pairs):
            if not node:
                return 0
            
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            
            if not node.right and not node.left:
                return 1 if len(pairs) <= 1 else 0
            
            return dfs(node.right, set(pairs)) + dfs(node.left, set(pairs))
        return dfs(root, set())
        
        
        
        
        
        
        
#         def isPal(li):
#             one = False
#             c = Counter(li)
#             for v in c.values():
#                 if v%2 == 1:
#                     if one:
#                         return False
#                     else:
#                         one = True
#             return True
            
#         def dfs(node, temp):
#             if not node:
#                 return 0
#             if not node.right and not node.left:
#                 if isPal(temp + [node.val]):
#                     return 1
#                 else:
#                     return 0
#             return dfs(node.right, temp+[node.val]) + dfs(node.left, temp+[node.val])
#         return dfs(root, [])
        