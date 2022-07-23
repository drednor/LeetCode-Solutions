class Solution:
    def countSubstrings(self, s: str) -> int:
        res  = 0
        flag = False
        if len(s) % 2 == 1:
            flag == True
        for i in range(len(s)):
            l , r = i , i
            # if flag:
            while l >= 0 and r<len(s) and s[l] == s[r]:
                # print("hello")
                res += 1
                l -= 1
                r += 1
            l , r = i , i+1
            while l >= 0  and r<len(s) and s[l] == s[r]:
                res+=1
                l -= 1
                r += 1

        return res