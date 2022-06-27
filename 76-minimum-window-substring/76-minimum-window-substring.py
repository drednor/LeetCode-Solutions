class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1+countT.get(c, 0)
        
        have , need = 0 , len(countT)
        res , reslen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c, 0)
            
            if c in countT and window[c]==countT[c]:
                have+=1
                
            while have == need:
                if (r-l+1)< reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]< countT[s[l]]:
                    have-=1
                l+=1
        l , r = res
        return s[l:r+1] if reslen != float("infinity") else ""
        
        
        
        # My attempt
        # if len(t)> len(s):
        #     return ""
        # if t in s:
        #     return t
        # c = Counter(t)
        # for r in range(len(t)-1,len(s)+1):
        #     l = 0
        #     while r<=len(s):
        #         if len(c&Counter(s[l:r+1]))==len(c):
        #             return s[l:r+1]
        #         r+=1
        #         l+=1
        # return ""