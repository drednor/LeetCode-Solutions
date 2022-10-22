class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if t == "":
            return ""
        l = 0 
        res = [-1,-1]
        reslen = float("inf")
        c = Counter(t)
        have = 0
        need = len(c)
        memo = {}
        for r in range(n):
            char = s[r]
            memo[char] = 1 + memo.get(char, 0)
            if char in c and memo[char] == c[char]:
                have += 1
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                memo[s[l]] -= 1
                if s[l] in c and memo[s[l]] < c[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""
                
                