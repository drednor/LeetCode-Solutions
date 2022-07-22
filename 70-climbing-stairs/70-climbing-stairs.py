class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n-1):
            temp = two
            two += one
            one = temp
        return two
        
        
        # memo = {}
        # def recur(x):
        #     if x in memo:
        #         return memo[x]
        #     if x == 0:
        #         return 1
        #     if x<0:
        #         return 0
        #     memo[x] = recur(x-1) + recur(x-2)
        #     return memo[x]
        # return recur(n)
        