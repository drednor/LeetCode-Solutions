class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def recur(i,j):
            key = (i,j)
            if i == len(s1) and j == len(s2):
                return True  
            if key in memo:
                return memo[key]
            if i < len(s1) and s1[i] == s3[i+j] and recur(i+1,j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and recur(i,j+1):
                return True
            memo[key] = False
            return False
        return recur(0,0)
        
        # memo = {}
        # def recur(i,j,k, sub):
        #     key = (i,j,k)
        #     if key in memo:
        #         return memo[key]
        #     if i == len(s1) and j == len(s2):
        #         if sub == s3:
        #             return True
        #         else:
        #             return False
        #     if k >= len(s3):
        #         return False
        #     left = False
        #     right = False
        #     if i < len(s1):
        #         if s1[i] == s3[k]:
        #             left = recur(i+1,j,k+1,sub+s1[i])
        #     if j < len(s2):
        #         if s2[j] == s3[k]:
        #             right = recur(i,j+1,k+1,sub+s2[j])
        #     memo[key] = left or right
        #     return memo[key]
        # return recur(0,0,0,"")
        

