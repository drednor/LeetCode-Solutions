class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recur(i,j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i == len(word1):
                memo[key] = len(word2) - j
            elif j == len(word2):
                memo[key] = len(word1) - i
            elif word1[i] == word2[j]:
                memo[key] = recur(i+1,j+1)
            else:
                memo[key] = 1+ min(recur(i+1,j+1),recur(i+1,j),recur(i,j+1))
            return memo[key]
        return(recur(0,0)) 