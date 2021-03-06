# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        while q:
            queue_len = len(q)
            level = []
            for item in range(queue_len):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                result.append(level)
        return result
        
        # q = deque()
        # q.append(root)
        # result = []
        # while q:
        #     qlen = len(q)
        #     level = []
        #     for i in range(qlen):
        #         cur = q.popleft()
        #         if cur:
        #             level.append(cur.val)
        #             q.append(cur.left)
        #             q.append(cur.right)
        #     if level:
        #         result.append(level)
        # return result
            