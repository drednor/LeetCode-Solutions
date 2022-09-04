# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0, 0))
        memo = {}
        while q:
            cur, r, c = q.popleft()
            key = (r,c)
            if key not in memo:
                memo[key] = []
            memo[key].append(cur.val)
            if cur.left:
                q.append((cur.left, r+1,c-1))
            if cur.right:
                q.append((cur.right, r+1, c+1))
        cols = defaultdict(list)
        res = []
        for x, y in sorted(memo.keys()):
            cols[y].extend(sorted(memo[(x,y)]))
        for key in sorted(cols.keys()):
            res.append(cols[key])
        
        # for key, val in sorted(memo.items()):
        #     if key[0] != old:
        #         res.append([])
        #     res[-1].extend(sorted(val))
        #     old = key[0]
        # #print(res)
        return res
            
        