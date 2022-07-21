class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        table = [None]*(n+1)
        table[0] = 0
        table[1] = 1
        for i in range(len(table)):
            if i+2 <len(table):
                table[i+2] = table[i] + table[i+1]
        return table[n]
                    
                                            
        # memo ={}
        # def recur(x):
        #     if x in memo:
        #         return memo[x]
        #     if x == 1:
        #         return 1
        #     if x == 0:
        #         return 0
        #     memo[x] = recur(x-1) + recur(x-2)
        #     return memo[x]
        # return recur(n)