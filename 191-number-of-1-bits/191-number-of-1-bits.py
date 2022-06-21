class Solution:
    def hammingWeight(self, n: int) -> int:
        # best solution the loop only runs
        # equal to the number of 1 in the number
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
        
        
        #going through all digits and adding 1 to the result when we find a 1 
        # bit shift using >> or divide it by 2
        # res = 0
        # while n:
        #     res += n%2
        #     n = n>>1
        #     #n = n // 2
        # return res
        
        
        #SIMPLE SOLUTION
        # c = Counter(str(bin(n)))
        # # print(n)
        # return int(c["1"])