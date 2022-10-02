class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        mod = 10**9 + 7
        res = [0]
        def recur(i, total):
            key = (i,total)
            if key in memo:
                return memo[key]
            if i == 0 and total != 0:
                return 0
            if total == 0 and i == 0:
                return 1
            if total == 0 and i != 0:
                return 0
            temp = 0
            for j in range(1,k+1):
                temp += recur(i-1,total-j)
            memo[key] = temp
            return memo[key]
        ans = recur(n,target)
        return ans%mod