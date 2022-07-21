class Solution:
    def fib(self, n: int) -> int:
        memo ={}
        def recur(x):
            if x in memo:
                return memo[x]
            if x == 1:
                return 1
            if x == 0:
                return 0
            memo[x] = recur(x-1) + recur(x-2)
            return memo[x]
        return recur(n)