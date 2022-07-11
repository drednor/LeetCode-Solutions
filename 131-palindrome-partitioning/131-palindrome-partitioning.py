class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(i, sub):
            if i >= len(s):
                result.append(sub)
                return
            for j in range(i,len(s)):
                if self.ispal(s[i:j+1]):
                    backtrack(j+1,sub+[s[i:j+1]])
            
        backtrack(0,[])
        return result
        
    def ispal(self, s):
        return s==s[::-1]