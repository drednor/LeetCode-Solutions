class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
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