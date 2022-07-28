class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def recur(i, j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = 0
            if t[j] == s[i]:
                res += recur(i+1,j+1)
            res += recur(i+1,j)
            memo[key] = res
            return memo[key]
        return recur(0,0)