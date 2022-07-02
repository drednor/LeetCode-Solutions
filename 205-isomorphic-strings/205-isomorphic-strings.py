class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp ={}
        temp2 = {}
        for i in range(len(s)):
            if s[i] in temp and temp[s[i]] != t[i]:
                return False
            if t[i] in temp2 and temp2[t[i]] != s[i]:
                return False
            temp[s[i]] = t[i]
            temp2[t[i]] = s[i]
        return True