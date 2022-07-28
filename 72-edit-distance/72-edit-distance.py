class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(table)):
            if i+1 < len(table):
                table[i+1][0] = i+1
            for j in range(len(table[0])):
                if j+1 < len(table[0]):
                    table[0][j+1] = j+1
                if i+1<len(table) and j+1<len(table[0]):
                    if word2[i] == word1[j]:
                        table[i+1][j+1] = table[i][j]
                    else:
                        table[i+1][j+1] = 1 + min(table[i][j],table[i+1][j],table[i][j+1])
        return table[-1][-1]
        
        
        # memo = {}
        # def recur(i,j):
        #     key = (i,j)
        #     if key in memo:
        #         return memo[key]
        #     if i == len(word1):
        #         memo[key] = len(word2) - j
        #     elif j == len(word2):
        #         memo[key] = len(word1) - i
        #     elif word1[i] == word2[j]:
        #         memo[key] = recur(i+1,j+1)
        #     else:
        #         memo[key] = 1+ min(recur(i+1,j+1),recur(i+1,j),recur(i,j+1))
        #     return memo[key]
        # return(recur(0,0)) 