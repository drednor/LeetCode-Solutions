class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def recur(i, j, sub):
            key = (i,j)
            if key in memo:
                return memo[key]
            if sub == t:
                return 1
            if i == len(s):
                return 0
            res = 0
            if t[j:].startswith(s[i]):
                res += recur(i+1,j+1,sub + s[i])
            res += recur(i+1,j,sub)
            memo[key] = res
            return memo[key]
        return recur(0,0,"")