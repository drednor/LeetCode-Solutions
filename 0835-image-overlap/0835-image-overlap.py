class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def helper(x,y):
            num = 0
            for r in range(n):
                for c in range(n):
                    if 0<=x+r<n and 0<=y+c<n and img1[x+r][y+c] == 1 and img2[r][c] == 1:
                        num += 1
            return num
        
        return max(helper(x,y) for x in range(-n,n) for y in range(-n,n))