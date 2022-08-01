class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0] * (n+1) for _ in range(m+1)]
        table[1][1] = 1
        for i in range(len(table)):
            for j in range(len(table[0])):
                if i-1>=0:
                    table[i][j] += table[i-1][j]
                if j-1>=0:
                    table[i][j] += table[i][j-1]
        return table[-1][-1]
   
        
        # memo = {}
        # def dfs(i,j):
        #     key = (i,j)
        #     if key in memo:
        #         return memo[key]
        #     if i == 1 and j == 1:
        #         return 1
        #     if i == 0 or j == 0:
        #         return 0
        #     memo[key] = dfs(i-1,j) + dfs(i, j-1)
        #     return memo[key]
        # return dfs(m,n)
        

        # table = [[0]*(m+1) for _ in range(n+1)]
        # table[1][1] = 1
        # for i in range(len(table)):
        #     for j in range(len(table[0])):
        #         if i+1<len(table):
        #             table[i+1][j] += table[i][j]
        #         if j+1<len(table[0]):
        #             table[i][j+1] += table[i][j]
        # return table[-1][-1]
        
        
        
        
        
#         memo = {}
#         def recur(i,j):
#             key = (i,j)
#             if key in memo:
#                 return memo[key]
#             if i == 1 and j == 1:
#                 return 1
#             if i == 0 or j == 0:
#                 return 0
#             memo[key] = recur(i-1,j) + recur(i,j-1)
#             return memo[key]
#         return recur(m,n)
                   
        
  
        
        
        # memo = {}
        # def recur(r,c):
        #     key = (r,c)
        #     if key in memo:
        #         return memo[key]
        #     if r == 1 and c == 1:
        #         return 1
        #     if r == 0 or c == 0:
        #         return 0
        #     memo[key] = recur(r-1,c) + recur(r,c-1)
        #     return memo[key]
        # return recur(m,n)