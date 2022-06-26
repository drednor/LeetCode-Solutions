class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#         count ={}
#         result = 0
#         l = 0 
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r],0)
            
#             if (r-l+1)-max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1
#             result = max(r-l+1,result)
#         return result
    
    
        count = {}
        result = 0
        max_f =0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            max_f = max(count[s[r]], max_f)
            
            if (r-l+1)-max_f > k:
                count[s[l]] -= 1
                l+=1
            result = max(result, r-l+1)
        return result
                
                
        