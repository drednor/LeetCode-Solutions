class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a &= mask
        while b:
            temp = ((a & b) << 1) & mask 
            a = (a^b) & mask
            b = temp
        if (a>>31) & 1:
            return ~(a^mask)
        return a
        