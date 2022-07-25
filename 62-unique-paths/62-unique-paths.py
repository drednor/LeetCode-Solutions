class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def recur(i,j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i == 1 and j == 1:
                return 1
            if i == 0 or j == 0:
                return 0
            memo[key] = recur(i-1,j) + recur(i,j-1)
            return memo[key]
        return recur(m,n)
                   
        
  
        
        
        # memo = {}
        # def recur(r,c):
        #     key = (r,c)
        #     if key in memo:
        #         return memo[key]
        #     if r == 1 and c == 1:
        #         return 1
        #     if r == 0 or c == 0:
        #         return 0
        #     memo[key] = recur(r-1,c) + recur(r,c-1)
        #     return memo[key]
        # return recur(m,n)