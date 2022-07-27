class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def recur(i,j,k, sub):
            key = (i,j,k)
            if key in memo:
                return memo[key]
            if i == len(s1) and j == len(s2):
                if sub == s3:
                    return True
                else:
                    return False
            if k >= len(s3):
                return False
            left = False
            right = False
            if i < len(s1):
                if s1[i] == s3[k]:
                    left = recur(i+1,j,k+1,sub+s1[i])
            if j < len(s2):
                if s2[j] == s3[k]:
                    right = recur(i,j+1,k+1,sub+s2[j])
            memo[key] = left or right
            return memo[key]
        return recur(0,0,0,"")
        

        # if len(s1) == 0 and len(s2) == 0:
        #     if len(s3) == 0:
        #         return True
        #     return False
        # if len(s1) == 0:
        #     if s2 == s3:
        #         return True
        #     else:
        #         return False
        # elif len(s2) == 0:
        #     if s1 == s3:
        #         return True
        #     else:
        #         return False
        # i = 0 
        # j = 0
        # k = 0
        # while k < len(s3):
        #     if i<len(s1) and s1[i] == s3[k]: 
        #         while i<len(s1) and s1[i] == s3[k]:
        #             i+=1
        #             k+=1
        #     elif j<len(s2) and s2[j] == s3[k]:
        #         while j<len(s2) and s2[j] == s3[k]:
        #             j+=1
        #             k+=1
        #     else:
        #         return False
        # return True if len(s1) == i and len(s2) == j and len(s3) == k else False