class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    table[i+1][j+1] = 1 + table[i][j]
                else:
                    table[i+1][j+1] = max(table[i+1][j],table[i][j+1])
        return table[-1][-1]
        
        
        
        
#         memo = {}
#         def recur(i,j):
#             key = (i,j)
#             if key in memo:
#                 return memo[key]
#             if i == len(text1) or j == len(text2):
#                 return 0
#             elif text1[i] == text2[j]:
#                 memo[key] = 1 + recur(i+1,j+1)
#             else :
#                 memo[key] = max(recur(i+1,j),recur(i,j+1))
#             return memo[key]
#         return recur(0,0)
            
        
        
        
        