class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        result = [0]
        def recur(sub):
            if sub in memo:
                return memo[sub]
            if len(sub) == 0:
                return 1
            if sub[0] == "0":
                return 0
            result[0] = recur(sub[1:])
            #print(sub, result[0])
            if len(sub) > 1:
                if sub[0] == "1" or sub[0] == "2" and sub[1] in "0123456":
                    #print("inside", sub[0], sub[1], result[0])
                    result[0] += recur(sub[2:])
            memo[sub] = result[0] 
            return result[0]
        return recur(s)
            
#         i = 0
#         for j in range(len(s)):
            
            
#             while i < len(s):
#                 if i+1 < len(s):
#                     if s[i+1] != "0":
#                         i+=1
#                     else:
#                         i+=2
            
#             while k < len(s):
#                 if k+2 < len(s):
#                     if s[k+2] != "0" and 0<int(s[:k+2]) <= 26:
                        
                    
        