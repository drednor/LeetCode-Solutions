"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append((root,0))
        res = {}
        while q:
            cur, i= q.popleft()
            if i not in res:
                res[i] = []
            res[i].append(cur.val)
            i+=1
            if cur.children:
                for child in cur.children:
                    q.append((child, i))
        ans = []
        for val in res.values():
            ans.append(val)
        return ans
            