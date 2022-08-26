class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        top = 1000000000
        i = 1
        check = []
        while i <= top:
            temp = Counter(str(i))
            check.append(temp)
            i *= 2
        c = Counter(str(n))
        if c in check:
            return True
        return False
        
        
        