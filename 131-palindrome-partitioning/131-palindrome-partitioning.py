class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(i, sub):
            if i >= len(s):
                #print(sub)
                result.append(sub)
                return
            for j in range(i,len(s)):
                if self.ispal(s[i:j+1]):
                    #print("current stering = ", s[i:j+1])
                    backtrack(j+1,sub+[s[i:j+1]])
            
        backtrack(0,[])
        return result
        
    def ispal(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True