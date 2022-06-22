class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask = 0xffffffff
        # while b:
        #     temp = ((a & b) << 1) & mask 
        #     a = (a^b) & mask
        #     b = temp
        # if (a>>31) & 1:
        #     return ~(a^mask)
        # return a
        mask = 0xffffffff
        a&=mask
        while b:
            sum1 = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum1
            b = carry
            
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a