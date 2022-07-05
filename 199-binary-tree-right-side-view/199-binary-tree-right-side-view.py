# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            qlen= len(q)
            rightside = None
            for i in range(qlen):
                cur = q.popleft()
                if cur:
                    rightside = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if rightside:
                result.append(rightside.val)
        return result