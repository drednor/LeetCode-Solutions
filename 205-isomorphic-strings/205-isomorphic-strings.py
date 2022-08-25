class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo = {}
        memo2 = {}
        for i in range(len(s)):
            if s[i] in memo and memo[s[i]] != t[i]:
                return False
            if t[i] in memo2 and memo2[t[i]] != s[i]:
                return False
            memo[s[i]] = t[i]
            memo2[t[i]] = s[i]
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        temp ={}
        temp2 = {}
        for i in range(len(s)):
            if s[i] in temp and temp[s[i]] != t[i]:
                return False
            if t[i] in temp2 and temp2[t[i]] != s[i]:
                return False
            temp[s[i]] = t[i]
            temp2[t[i]] = s[i]
        return True