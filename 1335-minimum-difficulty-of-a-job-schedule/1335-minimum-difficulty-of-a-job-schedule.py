class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        @lru_cache(None)
        def dp(i,d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n-d+1):
                maxd = max(maxd,jobDifficulty[j])
                res = min(res, maxd+dp(j+1,d-1))
            return res
        return dp(0,d)
            
            
            