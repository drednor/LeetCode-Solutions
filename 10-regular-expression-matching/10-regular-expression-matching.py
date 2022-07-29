class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def recur(i,j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1<len(p) and p[j+1] == "*":
                memo[key] = recur(i,j+2) or (match and recur(i+1,j))
                return memo[key]
            if match:
                memo[key] = recur(i+1,j+1)
                return memo[key]
            memo[key] = False
            return memo[key]                
        return recur(0,0)