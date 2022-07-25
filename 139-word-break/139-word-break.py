class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def recur(sub):
            if sub in memo:
                return memo[sub]
            if len(sub) == 0:
                return True
            for word in wordDict:
                if sub.startswith(word):
                    memo[sub[len(word):]] = recur(sub[len(word):])
                    if memo[sub[len(word):]]:
                        return True
            memo[sub] = False
            return False
        return recur(s)