class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for i in range(len(s)):
            temp = [1, i]
            if s[i] not in memo:
                memo[s[i]] = temp
            else:
                memo[s[i]][0] += 1
        for val in memo.values():
            x1, x2 = val
            if x1 == 1:
                return x2
        return -1
        