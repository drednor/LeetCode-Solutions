# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((0,root))
        res = {}
        while q:
            i, cur = q.popleft()
            if i not in res:
                res[i] = []
            res[i].append(cur.val)
            if cur.left:
                q.append((i+1,cur.left))
            if cur.right:
                q.append((i+1,cur.right))
        ans = []
        for key, val in res.items():
            ans.append(sum(val)/len(val))
        return ans