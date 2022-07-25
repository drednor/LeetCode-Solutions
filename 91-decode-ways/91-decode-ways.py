class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            print(s[i])
            if i+1<len(s):
                if s[i] == "1" or s[i] == "2" and s[i+1] in "0123456":
                    #print("inside", s[i],s[i+1])
                    dp[i] += dp[i+2]
            
        return dp[0]
        
        
        
        # memo = {}
        # result = [0]
        # def recur(sub):
        #     if sub in memo:
        #         return memo[sub]
        #     if len(sub) == 0:
        #         return 1
        #     if sub[0] == "0":
        #         return 0
        #     result[0] = recur(sub[1:])
        #     #print(sub, result[0])
        #     if len(sub) > 1:
        #         if sub[0] == "1" or sub[0] == "2" and sub[1] in "0123456":
        #             #print("inside", sub[0], sub[1], result[0])
        #             result[0] += recur(sub[2:])
        #     memo[sub] = result[0] 
        #     return result[0]
        # return recur(s)
            

                        
                    
        