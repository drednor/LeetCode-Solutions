# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left)and self.isSameTree(p.right, q.right))
        # que = deque()
        # que.append((p,q))
        # while que:
        #     first, second = que.popleft()
        #     if first.val != second.val:
        #         return False
        #     if first.right:
        #         if second.right:
        #             que.append((first.right,second.right))
        #         else:
        #             return False
        #     if second.right:
        #         if first.right:
        #             pass
        #         else:
        #             return False
        #     if first.left:
        #         if second.left:
        #             que.append((first.left,second.left))
        #         else:
        #             return False
        #     if second.left:
        #         if first.left:
        #             pass
        #         else:
        #             return False
        # return True