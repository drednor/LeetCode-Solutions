class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        l, r = 0 , len(s1)-1
        while r<len(s2):
            temp = Counter(s2[l:r+1])
            if temp == c:
                return True
            r+=1
            l+=1
        return False
        