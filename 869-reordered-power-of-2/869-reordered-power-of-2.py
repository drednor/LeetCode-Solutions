class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i = 1
        c = Counter(str(n))
        while i <= 10**9:
            temp = Counter(str(i))
            if temp == c:
                return True
            i *= 2
        return False
        
        