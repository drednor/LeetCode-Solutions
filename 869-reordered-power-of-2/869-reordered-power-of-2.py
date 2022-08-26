class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        top = 1000000000
        i = 1
        c = Counter(str(n))
        check = []
        while i <= top:
            temp = Counter(str(i))
            if temp == c:
                return True
            i *= 2
        return False
        
        # if c in check:
        #     return True
        # return False
        
        
        