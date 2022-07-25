class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False] * (len(s)+1)
        table[0] = True
        for i in range(len(s)):
            if table[i]:
                for word in wordDict:
                    #print(word)
                    if s[i:].startswith(word):
                        temp = i + len(word)
                        if temp < len(table):
                            table[temp] = True
        #print(table)
        return table[-1]
        
        
        
        
        
        # memo = {}
        # def recur(sub):
        #     if sub in memo:
        #         return memo[sub]
        #     if len(sub) == 0:
        #         return True
        #     for word in wordDict:
        #         if sub.startswith(word):
        #             memo[sub[len(word):]] = recur(sub[len(word):])
        #             if memo[sub[len(word):]]:
        #                 return True
        #     memo[sub] = False
        #     return False
        # return recur(s)