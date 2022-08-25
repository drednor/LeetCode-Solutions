class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(t)):
            if len(s) == j:
                return True
            if s[j] == t[i]:
                j+=1
        return j == len(s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # i = 0
        # j = 0
        # while i < len(s) and j<len(t):
        #     if s[i] == t[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         j+=1
        # if i == len(s):
        #     return True
        # else:
        #     return False