class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = 0
        num = len(columnTitle)
        res = 1
        while i <= len(columnTitle)-1:
            temp = ord(columnTitle[i]) - ord("A") + 1
            res += (26**(num-1) * temp)
            num -= 1
            i+=1
        return res-1
        #for i in range(num):
            