class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 3 ** 19
        return n > 0 and x % n == 0
        # i = 0
        # while 3**i<=n:
        #     print(bin(3**i))
        #     if 3**i == n:
        #         return True
        #     i+=1
        # return False
            
            