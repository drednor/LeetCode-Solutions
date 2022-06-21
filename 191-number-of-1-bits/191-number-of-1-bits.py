class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n>>1
            #n = n // 2
        return res
        
        
        #SIMPLE SOLUTION
        # c = Counter(str(bin(n)))
        # # print(n)
        # return int(c["1"])