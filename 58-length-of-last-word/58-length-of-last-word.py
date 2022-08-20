class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # last = s.split()
        # return len(last[-1])
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                for j in range(i,-1,-1):
                    if s[j] == " ":
                        return res
                    res+=1
                return res
        return res