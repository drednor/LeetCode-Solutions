class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordict = {}
        res = [] 
        for i in range(len(words)):
            wordict[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                    res.append([i,wordict[tmp1[::-1]]])
                if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]],i])

        return res
#         res = []
#         def check(s,i,j):
#             while i < j:
#                 if s[i] != s[j]:
#                     return False
#                 i+=1
#                 j-=1
#             return True
#         memo = {word:i for i, word in enumerate(words)}
#         for i in range(len(words)):
#             if words[i] == "":
#                 for j in range(len(words)):
#                     if i!=j and check(words[j],0, len(words[j])-1):
#                         res.append([i,j])
#                         res.append([j,i])
#                 continue
                
#             if words[i][::-1] in memo and memo[words[i][::-1]] != i:
#                 res.append([i,memo[words[i][::-1]]])
                
#             for k in range(1, len(words[i])):
#                 if check(words[i],0,k-1) and words[i][k:][::-1] in memo:
#                     res.append([memo[words[i][k:][::-1]],i])
#                 if check(words[i], k , len(words[i])-1) and words[i][:k][::-1] in memo:
#                     res.append([i,memo[words[i][:k][::-1]]])
#         return res